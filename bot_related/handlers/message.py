import aiogram
import dotenv
import ww_casino.bot_related.useful.misc as misc
import ww_casino.bot_related.useful.keyboards as keyboards
import ww_casino.db as db

dotenv.load_dotenv()

router = aiogram.Router()


@router.callback_query(aiogram.F.data == 'currencies_page1')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    user_db = db.DB()
    user_db.reopen_cursor_and_connection()

    await callback.message.edit_text(text="*1*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[0],
                     parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    user_db.close_cursor_and_connection()
    del user_db


@router.callback_query(aiogram.F.data == 'currencies_page2')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    user_db = db.DB()
    user_db.reopen_cursor_and_connection()

    await callback.message.edit_text(
        text="*2*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[1],
        parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    user_db.close_cursor_and_connection()
    del user_db


@router.callback_query(aiogram.F.data == 'currencies_page3')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    user_db = db.DB()
    user_db.reopen_cursor_and_connection()

    await callback.message.edit_text(
        text="*3*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[2],
        parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    user_db.close_cursor_and_connection()
    del user_db


@router.callback_query(aiogram.F.data == 'currencies_page4')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    user_db = db.DB()
    user_db.reopen_cursor_and_connection()

    await callback.message.edit_text(
        text="*4*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[3],
        parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    user_db.close_cursor_and_connection()
    del user_db


@router.callback_query(aiogram.F.data == 'currencies_page5')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    user_db = db.DB()
    user_db.reopen_cursor_and_connection()

    await callback.message.edit_text(
        text="*5*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[4],
        parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    user_db.close_cursor_and_connection()
    del user_db


@router.callback_query(aiogram.F.data == 'currencies_page6')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    user_db = db.DB()
    user_db.reopen_cursor_and_connection()

    await callback.message.edit_text(
        text="*6*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[5],
        parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    user_db.close_cursor_and_connection()
    del user_db


@router.callback_query(aiogram.F.data == 'currencies_page7')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    user_db = db.DB()
    user_db.reopen_cursor_and_connection()

    await callback.message.edit_text(
        text="*7*\nВаш баланс:\n" + misc.get_formatted_currencies_pages(user_db.get_balance('all'))[6],
        parse_mode='Markdown', reply_markup=keyboards.currencies_pages)

    user_db.close_cursor_and_connection()
    del user_db
