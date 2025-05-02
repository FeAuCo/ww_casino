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
    await msg.answer('Чтобы посмотреть баланс, введите команду: `/get {валюта}`\n'
                     'Чтобы пополнить баланс, введите команду: `/add {валюта} {количество}`\n'
                     '*Примечания:* \n*1.* Чтобы add работала корректно вы должны ввести название валюты именно так, как она предоставляется при выводе баланса\n'
                     '*2.* Если вы в `/get` введете `all`, вы увидите все валюты', parse_mode='Markdown')


@router.message()
async def add_command(msg: aiogram.types.Message):
    parameters = msg.text[4:].strip()
    user_db = db.DB()

    if msg.text[:4] == '/get':
        user_db.reopen_cursor_and_connection()

        if user_db.if_registered_check(msg.chat.id):
            user_db.add_user(msg.chat.id, datetime.datetime.today().strftime("%Y-%m-%d"))

            user_db.commit()

        if parameters == 'all':
            await msg.answer(text="*1*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[0], parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

        elif parameters in misc.currencies:
            await msg.answer(text=f"У вас *{user_db.get_balance(parameters)} {parameters}*", parse_mode='Markdown')

        else:
            await msg.answer(text='Мы не предоставляем оплату этой валютой. Возможно вы ввели название валюты неверно')

        user_db.close_cursor_and_connection()

    elif msg.text[:4] == '/add':
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
                await msg.answer(text='Мы не предоставляем оплату этой валютой. Возможно вы ввели название валюты неверно')

        except ValueError:
            await msg.answer(text='Вы ввели некорректную или равную нулю сумму')
