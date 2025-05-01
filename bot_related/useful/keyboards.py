import aiogram

mode1 = aiogram.types.InlineKeyboardButton(text='Правила 1 режима', callback_data='mode1')
mode2 = aiogram.types.InlineKeyboardButton(text='Правила 2 режима', callback_data='mode2')
mode3 = aiogram.types.InlineKeyboardButton(text='Правила 3 режима', callback_data='mode3')
mode4 = aiogram.types.InlineKeyboardButton(text='Правила 4 режима', callback_data='mode4')

modes_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[mode1, mode2],
                                                                            [mode3, mode4]])

currency_previous_page = aiogram.types.InlineKeyboardButton(text='<-', callback_data='currency_previous_page')
currency_next_page = aiogram.types.InlineKeyboardButton(text='->', callback_data='currency_next_page')

currency_TONCOIN = aiogram.types.InlineKeyboardButton(text='TONCOIN', callback_data='TONCOIN')
currency_XROCK = aiogram.types.InlineKeyboardButton(text='XROCK', callback_data='XROCK')
currency_SCALE = aiogram.types.InlineKeyboardButton(text='SCALE', callback_data='SCALE')
currency_BOLT = aiogram.types.InlineKeyboardButton(text='BOLT', callback_data='BOLT')
currency_TAKE = aiogram.types.InlineKeyboardButton(text='TAKE', callback_data='TAKE')
currency_TNX = aiogram.types.InlineKeyboardButton(text='TNX', callback_data='TNX')
currency_GRBS = aiogram.types.InlineKeyboardButton(text='GRBS', callback_data='GRBS')
currency_JBCT = aiogram.types.InlineKeyboardButton(text='JBCT', callback_data='JBCT')
currency_IVS = aiogram.types.InlineKeyboardButton(text='IVS', callback_data='IVS')
currency_BTC = aiogram.types.InlineKeyboardButton(text='BTC', callback_data='BTC')
currency_ANON = aiogram.types.InlineKeyboardButton(text='ANON', callback_data='ANON')
currency_ATL = aiogram.types.InlineKeyboardButton(text='ATL', callback_data='ATL')
currency_NUDES = aiogram.types.InlineKeyboardButton(text='NUDES', callback_data='NUDES')
currency_WIF = aiogram.types.InlineKeyboardButton(text='WIF', callback_data='WIF')
currency_MARGA = aiogram.types.InlineKeyboardButton(text='MARGA', callback_data='MARGA')
currency_DUREV = aiogram.types.InlineKeyboardButton(text='DUREV', callback_data='DUREV')
currency_SOX = aiogram.types.InlineKeyboardButton(text='SOX', callback_data='SOX')
currency_UNIC = aiogram.types.InlineKeyboardButton(text='UNIC', callback_data='UNIC')
currency_VIRUS1 = aiogram.types.InlineKeyboardButton(text='VIRUS1', callback_data='VIRUS1')
currency_ICTN = aiogram.types.InlineKeyboardButton(text='ICTN', callback_data='ICTN')
currency_JMT = aiogram.types.InlineKeyboardButton(text='JMT', callback_data='JMT')
currency_FID = aiogram.types.InlineKeyboardButton(text='FID', callback_data='FID')
currency_CATS = aiogram.types.InlineKeyboardButton(text='CATS', callback_data='CATS')
currency_WALL = aiogram.types.InlineKeyboardButton(text='WALL', callback_data='WALL')
currency_NOT = aiogram.types.InlineKeyboardButton(text='NOT', callback_data='NOT')
currency_OPEN = aiogram.types.InlineKeyboardButton(text='OPEN', callback_data='OPEN')
currency_DHD = aiogram.types.InlineKeyboardButton(text='DHD', callback_data='DHD')
currency_KINGY = aiogram.types.InlineKeyboardButton(text='KINGY', callback_data='KINGY')
currency_GGT = aiogram.types.InlineKeyboardButton(text='GGT', callback_data='GGT')
currency_JETTON = aiogram.types.InlineKeyboardButton(text='JETTON', callback_data='JETTON')
currency_BNB = aiogram.types.InlineKeyboardButton(text='BNB', callback_data='BNB')
currency_USDT = aiogram.types.InlineKeyboardButton(text='USDT', callback_data='USDT')
currency_LIFEYT = aiogram.types.InlineKeyboardButton(text='LIFEYT', callback_data='LIFEYT')
currency_GEMSTON = aiogram.types.InlineKeyboardButton(text='GEMSTON', callback_data='GEMSTON')
currency_TRX = aiogram.types.InlineKeyboardButton(text='TRX', callback_data='TRX')
currency_PUNK = aiogram.types.InlineKeyboardButton(text='PUNK', callback_data='PUNK')
currency_TONNEL = aiogram.types.InlineKeyboardButton(text='TONNEL', callback_data='TONNEL')
currency_DFC = aiogram.types.InlineKeyboardButton(text='DFC', callback_data='DFC')
currency_ETH = aiogram.types.InlineKeyboardButton(text='ETH', callback_data='ETH')
currency_ARBUZ = aiogram.types.InlineKeyboardButton(text='ARBUZ', callback_data='ARBUZ')
currency_RAFF = aiogram.types.InlineKeyboardButton(text='RAFF', callback_data='RAFF')
currency_DRIFT = aiogram.types.InlineKeyboardButton(text='DRIFT', callback_data='DRIFT')
currency_FISH = aiogram.types.InlineKeyboardButton(text='FISH', callback_data='FISH')
currency_MEOW = aiogram.types.InlineKeyboardButton(text='MEOW', callback_data='MEOW')
currency_TINU = aiogram.types.InlineKeyboardButton(text='TINU', callback_data='TINU')
currency_GRAM = aiogram.types.InlineKeyboardButton(text='GRAM', callback_data='GRAM')
currency_WEB3 = aiogram.types.InlineKeyboardButton(text='WEB3', callback_data='WEB3')
currency_MRDN = aiogram.types.InlineKeyboardButton(text='MRDN', callback_data='MRDN')
currency_LKY = aiogram.types.InlineKeyboardButton(text='LKY', callback_data='LKY')
currency_STBL = aiogram.types.InlineKeyboardButton(text='STBL', callback_data='STBL')
currency_1RUSD = aiogram.types.InlineKeyboardButton(text='1RUSD', callback_data='1RUSD')
currency_JVT = aiogram.types.InlineKeyboardButton(text='JVT', callback_data='JVT')
currency_DRA = aiogram.types.InlineKeyboardButton(text='DRA', callback_data='DRA')
currency_STATHAM = aiogram.types.InlineKeyboardButton(text='STATHAM', callback_data='STATHAM')
currency_PLANKTON = aiogram.types.InlineKeyboardButton(text='PLANKTON', callback_data='PLANKTON')
currency_VWS = aiogram.types.InlineKeyboardButton(text='VWS', callback_data='VWS')
currency_SAU = aiogram.types.InlineKeyboardButton(text='SAU', callback_data='SAU')
currency_CAVI = aiogram.types.InlineKeyboardButton(text='CAVI', callback_data='CAVI')
currency_ALENKA = aiogram.types.InlineKeyboardButton(text='ALENKA', callback_data='ALENKA')
currency_TIME = aiogram.types.InlineKeyboardButton(text='TIME', callback_data='TIME')
currency_CES = aiogram.types.InlineKeyboardButton(text='CES', callback_data='CES')
currency_KKX = aiogram.types.InlineKeyboardButton(text='KKX', callback_data='KKX')
currency_HYDRA = aiogram.types.InlineKeyboardButton(text='HYDRA', callback_data='HYDRA')
currency_GRC = aiogram.types.InlineKeyboardButton(text='GRC', callback_data='GRC')
currency_tsTON = aiogram.types.InlineKeyboardButton(text='tsTON', callback_data='tsTON')
currency_STON = aiogram.types.InlineKeyboardButton(text='STON', callback_data='STON')
currency_DOGS = aiogram.types.InlineKeyboardButton(text='DOGS', callback_data='DOGS')
currency_SOL = aiogram.types.InlineKeyboardButton(text='SOL', callback_data='SOL')
currency_THNG = aiogram.types.InlineKeyboardButton(text='THNG', callback_data='THNG')
currency_SP = aiogram.types.InlineKeyboardButton(text='SP', callback_data='SP')
currency_AQUAXP = aiogram.types.InlineKeyboardButton(text='AQUAXP', callback_data='AQUAXP')
currency_CATI = aiogram.types.InlineKeyboardButton(text='CATI', callback_data='CATI')
currency_HMSTR = aiogram.types.InlineKeyboardButton(text='HMSTR', callback_data='HMSTR')
currency_STORM = aiogram.types.InlineKeyboardButton(text='STORM', callback_data='STORM')
currency_SPN = aiogram.types.InlineKeyboardButton(text='SPN', callback_data='SPN')
currency_JETTY = aiogram.types.InlineKeyboardButton(text='JETTY', callback_data='JETTY')
currency_MAJOR = aiogram.types.InlineKeyboardButton(text='MAJOR', callback_data='MAJOR')
currency_FTON = aiogram.types.InlineKeyboardButton(text='FTON', callback_data='FTON')
currency_CATSTG = aiogram.types.InlineKeyboardButton(text='CATSTG', callback_data='CATSTG')
currency_BUILD = aiogram.types.InlineKeyboardButton(text='BUILD', callback_data='BUILD')
currency_TRUMP = aiogram.types.InlineKeyboardButton(text='TRUMP', callback_data='TRUMP')
currency_MELANIA = aiogram.types.InlineKeyboardButton(text='MELANIA', callback_data='MELANIA')
currency_USDC = aiogram.types.InlineKeyboardButton(text='USDC', callback_data='USDC')
currency_WOOF = aiogram.types.InlineKeyboardButton(text='WOOF', callback_data='WOOF')

currency_page1_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currency_TONCOIN, currency_XROCK],
                                                                                     [currency_SCALE, currency_BOLT],
                                                                                     [currency_TAKE, currency_TNX],
                                                                                     [currency_GRBS, currency_JBCT],
                                                                                     [currency_IVS, currency_BTC],
                                                                                     [currency_ANON, currency_ATL],
                                                                                     [currency_next_page]])
currency_page2_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currency_NUDES, currency_WIF],
                                                                                     [currency_MARGA, currency_DUREV],
                                                                                     [currency_SOX, currency_UNIC],
                                                                                     [currency_VIRUS1, currency_ICTN],
                                                                                     [currency_JMT, currency_FID],
                                                                                     [currency_CATS, currency_WALL],
                                                                                     [currency_next_page,
                                                                                      currency_previous_page]])
currency_page3_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currency_NOT, currency_OPEN],
                                                                                     [currency_DHD, currency_KINGY],
                                                                                     [currency_GGT, currency_JETTON],
                                                                                     [currency_BNB, currency_USDT],
                                                                                     [currency_LIFEYT,
                                                                                      currency_GEMSTON],
                                                                                     [currency_TRX, currency_PUNK],
                                                                                     [currency_next_page,
                                                                                      currency_previous_page]])
currency_page4_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currency_TONNEL, currency_DFC],
                                                                                     [currency_ETH, currency_ARBUZ],
                                                                                     [currency_RAFF, currency_DRIFT],
                                                                                     [currency_FISH, currency_MEOW],
                                                                                     [currency_TINU, currency_GRAM],
                                                                                     [currency_WEB3, currency_MRDN],
                                                                                     [currency_next_page,
                                                                                      currency_previous_page]])
currency_page5_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currency_LKY, currency_STBL],
                                                                                     [currency_1RUSD, currency_JVT],
                                                                                     [currency_DRA, currency_STATHAM],
                                                                                     [currency_PLANKTON, currency_VWS],
                                                                                     [currency_SAU, currency_CAVI],
                                                                                     [currency_ALENKA, currency_TIME],
                                                                                     [currency_next_page,
                                                                                      currency_previous_page]])
currency_page6_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currency_CES, currency_KKX],
                                                                                     [currency_HYDRA, currency_GRC],
                                                                                     [currency_tsTON, currency_STON],
                                                                                     [currency_DOGS, currency_SOL],
                                                                                     [currency_THNG, currency_SP],
                                                                                     [currency_AQUAXP, currency_CATI],
                                                                                     [currency_next_page,
                                                                                      currency_previous_page]])
currency_page7_inline_keyboard = aiogram.types.InlineKeyboardMarkup(inline_keyboard=[[currency_HMSTR, currency_STORM],
                                                                                     [currency_SPN, currency_JETTY],
                                                                                     [currency_MAJOR, currency_FTON],
                                                                                     [currency_CATSTG, currency_BUILD],
                                                                                     [currency_TRUMP, currency_MELANIA],
                                                                                     [currency_USDC, currency_WOOF],
                                                                                     [currency_previous_page]])
