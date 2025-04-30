import asyncio
import json
import aiogram
import ww_casino.bot_related.useful.keyboards as keyboards
from aiogram.filters import CommandStart
import os
import requests
import psycopg2 as pg
import dotenv
import datetime

dotenv.load_dotenv()

router = aiogram.Router()


@router.message(CommandStart())
async def start_message(msg: aiogram.types.Message):
    await msg.answer('ДЕПАЕМ???', reply_markup=keyboards.modes_inline_keyboard)


@router.message()
async def add_message(msg: aiogram.types.Message):
    if msg.text[:3] == 'add' and len(msg.text) > 3 and msg.text[3:].strip().isdigit():
        invoice = requests.post(url='https://pay.xrocket.tg/tg-invoices',
                                headers={'Rocket-Pay-Key': os.getenv('XROCKET_TOKEN')},
                                json={
                                    'amount': msg.text[3:],
                                    'currency': "USDT",
                                    'description': "ПОПОЛНЯЕМ",
                                    'hiddenMessage': "СПАСИБО ЗА ПОПОЛНЕНИЕ БРАТ",
                                    'commentsEnabled': False,
                                    'expiredIn': 20
                                }).json()

        await msg.answer(invoice['data']['link'])

        while True:
            status = requests.get(url=f"https://pay.xrocket.tg/tg-invoices/{invoice['data']['id']}",
                                  headers={'Rocket-Pay-Key': os.getenv('XROCKET_TOKEN')}).json()['data']['status']

            if status == 'expired':
                break

            elif status == 'paid':
                connection = pg.connect(user='postgres', dbname='postgres', host='localhost',
                                        port=5432, password=os.getenv('POSTGRES_PASSWORD'))
                cursor = connection.cursor()

                cursor.execute(f'SELECT NOT EXISTS (SELECT {msg.chat.id} FROM "user")')

                if cursor.fetchone()[0]:
                    cursor.execute(
                        f'INSERT INTO "user" (chat_id, registration_date, balance) VALUES {msg.chat.id, datetime.datetime.today().strftime("%Y-%m-%d"), json.dumps({"USDT": int(msg.text[3:])})}')
                else:
                    cursor.execute("SELECT balance -> 'USDT' AS " + '"USDT" FROM "user"')

                    current_balance = cursor.fetchone()[0]

                    cursor.execute(
                        'UPDATE "user" SET balance = ' + f'jsonb_set(balance::jsonb, ' + "'{USDT}', " + f"'{int(msg.text[3:]) + current_balance}') " + f'WHERE "chat_id" = {msg.chat.id}')

                connection.commit()

                cursor.close()
                connection.close()

                break

        await asyncio.sleep(1)
