import asyncio
import json
import aiogram
import ww_casino.bot_related.useful.keyboards as keyboards
from aiogram.filters import CommandStart
import os
import requests
import dotenv
import datetime
import ww_casino.bot_related.useful.misc as misc
import ww_casino.db as db
import decimal

dotenv.load_dotenv()

router = aiogram.Router()


@router.message(CommandStart())
async def start_message(msg: aiogram.types.Message):
    await msg.answer('ДЕПАЕМ???', reply_markup=keyboards.modes_inline_keyboard)


@router.message()
async def add_message(msg: aiogram.types.Message):
    if len(msg.text) > 3:
        parameters = msg.text[3:].strip()
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

                if msg.text[:3] == 'add':
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
                                user_db = db.DB()

                                if user_db.if_registered_check(msg.chat.id):
                                    user_db.add_user(msg.chat.id, datetime.datetime.today().strftime("%Y-%m-%d"))
                                user_db.update_user_balance(msg.chat.id, currency, amount)

                                user_db.commit()

                                user_db.close_cursor_and_connection()

                                del user_db

                                break

                            await asyncio.sleep(1)

                    except KeyError:
                        await msg.answer(text='Количество валюты неприемлемо')

                else:
                    await msg.answer(text='Команда введена неверно')

            else:
                await msg.answer(text='Мы не предоставляем оплату этой валютой. Возможно вы ввели название валюты неверно')

        except ValueError:
            await msg.answer(text='Вы ввели некорректную или равную нулю сумму')

    else:
        await msg.answer(text='Команда введена неверно')
