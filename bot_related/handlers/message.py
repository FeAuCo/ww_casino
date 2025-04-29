import aiogram
import dotenv

dotenv.load_dotenv()

router = aiogram.Router()


@router.callback_query(aiogram.F.data == 'mode1')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    await callback.message.answer("Сколько хотите депнуть?")
    await callback.message.delete()


@router.callback_query(aiogram.F.data == 'mode2')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    await callback.message.answer("Сколько хотите депнуть?")
    await callback.message.delete()


@router.callback_query(aiogram.F.data == 'mode3')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    await callback.message.answer("Сколько хотите депнуть?")
    await callback.message.delete()


@router.callback_query(aiogram.F.data == 'mode4')
async def modes_reply(callback: aiogram.types.CallbackQuery):
    await callback.message.answer("Сколько хотите депнуть?")
    await callback.message.delete()
