import aiogram
import ww_casino.bot_related.useful.keyboards as keyboards
from aiogram.filters import CommandStart


router = aiogram.Router()


@router.message(CommandStart())
async def start_message(msg: aiogram.types.Message):
    await msg.answer('ДЕПАЕМ???', reply_markup=keyboards.modes_inline_keyboard)
