import aiogram

mode1 = aiogram.types.InlineKeyboardButton(text='Правила 1 режима', callback_data='mode1')
mode2 = aiogram.types.InlineKeyboardButton(text='Правила 2 режима', callback_data='mode2')
mode3 = aiogram.types.InlineKeyboardButton(text='Правила 3 режима', callback_data='mode3')
mode4 = aiogram.types.InlineKeyboardButton(text='Правила 4 режима', callback_data='mode4')

modes_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[mode1, mode2],
                                                                            [mode3, mode4]])
