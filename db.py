import psycopg2
import psycopg2 as pg
import os
import dotenv
import decimal
import json
import ww_casino.bot_related.useful.misc as misc

dotenv.load_dotenv()


class DB:
    connection = pg.connect(user='postgres', dbname='postgres', host='localhost',
                            port=5432, password=os.getenv('POSTGRES_PASSWORD'))
    cursor = connection.cursor()

    @staticmethod
    def if_registered_check(chat_id):
        try:
            DB.cursor.execute(f'SELECT NOT EXISTS (SELECT {chat_id} FROM "user")')

        except psycopg2.InterfaceError as ie:
            DB.reopen_cursor_and_connection()
            DB.cursor.execute(f'SELECT NOT EXISTS (SELECT {chat_id} FROM "user")')

        return True if DB.cursor.fetchone()[0] else False

    @staticmethod
    def add_user(chat_id, registration_date):
        DB.cursor.execute(
            f'INSERT INTO "user" (chat_id, registration_date, balance) VALUES {chat_id, registration_date, json.dumps({cur: 0 for cur in misc.currencies})}')

    @staticmethod
    def update_user_balance(chat_id, currency, amount):
        DB.cursor.execute(f"SELECT balance -> '{currency}' AS " + f'"{currency}" FROM "user"')

        current_balance = DB.cursor.fetchone()[0]

        DB.cursor.execute(
            'UPDATE "user" SET balance = ' + f'jsonb_set(balance::jsonb, ' + "'{" + f"{currency}" + "}', " + f"'{json.dumps(decimal.Decimal(str(current_balance)) + amount, ensure_ascii=False, default=str)}') " + f'WHERE "chat_id" = {chat_id}')

    @staticmethod
    def get_balance(currency='all'):
        if currency == 'all':
            DB.cursor.execute('SELECT balance FROM "user"')

        else:
            DB.cursor.execute(f"SELECT balance -> '{currency}' AS " + f'"{currency}" FROM "user"')

        return DB.cursor.fetchone()[0]


    # @staticmethod
    # def update_user_final_income():
    #

    @staticmethod
    def commit():
        DB.connection.commit()

    @staticmethod
    def reopen_cursor_and_connection():
        DB.connection = pg.connect(user='postgres', dbname='postgres', host='localhost',
                            port=5432, password=os.getenv('POSTGRES_PASSWORD'))
        DB.cursor = DB.connection.cursor()

    @staticmethod
    def close_cursor_and_connection():
        DB.cursor.close()
        DB.connection.close()
