import aiogram

mode1 = aiogram.types.InlineKeyboardButton(text='БИГ ПАПА ДЕП', callback_data='mode1')

modes_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[mode1]])
