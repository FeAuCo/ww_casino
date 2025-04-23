import aiogram
import requests
import os
import dotenv

dotenv.load_dotenv()
router = aiogram.Router()


@router.callback_query(aiogram.F.data == 'mode1')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    await callback.message.answer(requests.post(url='https://pay.xrocket.tg/tg-invoices',
                                                headers={'Rocket-Pay-Key': os.getenv('XROCKET_TOKEN')},
                                                json={
                                                    'amount': 500,
                                                    'currency': "USDT",
                                                    'description': "ДЕПАЕМ БРАТ",
                                                    'hiddenMessage': "СПАСИБО ЗА ДЕП БРАТ",
                                                    'commentsEnabled': False,
                                                    'expiredIn': 20
                                                }).json()['data']['link'])
