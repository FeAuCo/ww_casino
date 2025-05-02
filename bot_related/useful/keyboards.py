import aiogram

mode1 = aiogram.types.InlineKeyboardButton(text='Правила 1 режима', callback_data='mode1')
mode2 = aiogram.types.InlineKeyboardButton(text='Правила 2 режима', callback_data='mode2')
mode3 = aiogram.types.InlineKeyboardButton(text='Правила 3 режима', callback_data='mode3')
mode4 = aiogram.types.InlineKeyboardButton(text='Правила 4 режима', callback_data='mode4')

currencies_page1 = aiogram.types.InlineKeyboardButton(text='1', callback_data='currencies_page1')
currencies_page2 = aiogram.types.InlineKeyboardButton(text='2', callback_data='currencies_page2')
currencies_page3 = aiogram.types.InlineKeyboardButton(text='3', callback_data='currencies_page3')
currencies_page4 = aiogram.types.InlineKeyboardButton(text='4', callback_data='currencies_page4')
currencies_page5 = aiogram.types.InlineKeyboardButton(text='5', callback_data='currencies_page5')
currencies_page6 = aiogram.types.InlineKeyboardButton(text='6', callback_data='currencies_page6')
currencies_page7 = aiogram.types.InlineKeyboardButton(text='7', callback_data='currencies_page7')

currencies_pages = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currencies_page1, currencies_page2],
                                                                       [currencies_page3, currencies_page4],
                                                                       [currencies_page5, currencies_page6],
                                                                       [currencies_page7]])
