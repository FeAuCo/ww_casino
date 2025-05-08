import asyncio
import json
import aiogram
from aiogram.filters import CommandStart
import os
import requests
import dotenv
import datetime
import ww_casino.bot_related.useful.misc as misc
import ww_casino.bot_related.useful.keyboards as keyboards
import ww_casino.db as db
import decimal

dotenv.load_dotenv()

router = aiogram.Router()


@router.message(CommandStart())
async def start_command(msg: aiogram.types.Message):
    await msg.answer('*ДОБРО ПОЖАЛОВАТЬ В НАШ КАЗИК*\n\n'
                     'Введите `/help`, чтобы ознакомиться',
                     parse_mode='Markdown')


@router.message(aiogram.filters.Command('add'))
async def add_command(msg: aiogram.types.Message):
    parameters = msg.text[4:].strip()
    user_db = db.DB()

    user_db.reopen_cursor_and_connection()

    currency = []

    for char in parameters:
        if not char.isalpha():
            break

        currency.append(char)

    currency = ''.join(currency)
    amount = ''.join([digit for digit in parameters[len(currency):] if digit != ' '])

    try:
        amount = float(amount)
        amount = decimal.Decimal(str(amount))

        if currency in misc.currencies:

            invoice = requests.post(url='https://pay.xrocket.tg/tg-invoices',
                                    headers={'Rocket-Pay-Key': os.getenv('XROCKET_TOKEN')},
                                    json={
                                        'amount': float(json.dumps(decimal.Decimal(str(amount)), ensure_ascii=False, default=str)[1:-1]),
                                        'currency': currency,
                                        'description': "ПОПОЛНЯЕМ?",
                                        'hiddenMessage': "СПАСИБО ЗА ПОПОЛНЕНИЕ БРАТ",
                                        'commentsEnabled': False,
                                        'expiredIn': 20
                                    }).json()
            try:
                await msg.answer(invoice['data']['link'])

                while True:
                    status = requests.get(url=f"https://pay.xrocket.tg/tg-invoices/{invoice['data']['id']}",
                                          headers={'Rocket-Pay-Key': os.getenv('XROCKET_TOKEN')}).json()['data']['status']

                    if status == 'expired':
                        break

                    elif status == 'paid':
                        if user_db.if_registered_check(msg.chat.id):
                            user_db.add_user(msg.chat.id, datetime.datetime.today().strftime("%Y-%m-%d"))
                        user_db.update_user_balance(msg.chat.id, currency, amount)

                        user_db.commit()

                        user_db.close_cursor_and_connection()

                        break

                    await asyncio.sleep(1)

            except KeyError:
                await msg.answer(text='Количество валюты неприемлемо')

        else:
            await msg.answer(text='Мы не работаем с этой валютой. Возможно, вы ввели название валюты неверно')

    except ValueError:
        await msg.answer(text='Вы ввели некорректную или равную нулю сумму')


@router.message(aiogram.filters.Command('get'))
async def get_command(msg: aiogram.types.Message):
    parameters = msg.text[4:].strip()
    user_db = db.DB()

    user_db.reopen_cursor_and_connection()

    if user_db.if_registered_check(msg.chat.id):
        user_db.add_user(msg.chat.id, datetime.datetime.today().strftime("%Y-%m-%d"))

        user_db.commit()

    if parameters == 'all':
        await msg.answer(text="*1*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[0],
                         parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    elif parameters in misc.currencies:
        await msg.answer(text=f"У вас *{user_db.get_balance(parameters)} {parameters}*", parse_mode='Markdown')

    else:
        await msg.answer(text='Мы не работаем с этой валютой. Возможно, вы ввели название валюты неверно')

    user_db.close_cursor_and_connection()


@router.message(aiogram.filters.Command('help'))
async def help_command(msg: aiogram.types.Message):
    await msg.answer(text='*Команда* `/get`*:*\n'
                          'Введите `/get all`, чтобы узнать ваш баланс во всех приемлемых валютах\n'
                          'Введите `/get {валюта}`, чтобы узнать ваш баланс в валюте, которую вы указали\n\n'
                          '*Команда* `/add`*:*\n'
                          'Введите `/add {валюта} {количество}`, чтобы пополнить баланс в указанной валюте\n\n'
                          '*Примечания:*\n'
                          '*1.* Фигурные скобки нигде вводить не нужно\n'
                          '*2.* Вы должны вводить валюты именно так, как они выводятся при `/get all`',
                     parse_mode='Markdown')
