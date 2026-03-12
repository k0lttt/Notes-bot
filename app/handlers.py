from aiogram import F, Router
from aiogram.filters import Command, CommandStart
from aiogram.types import Message, CallbackQuery

from . import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я твой бот помошник! Я буду напоминать тебе о важных событиях.", 
        reply_markup=kb.main
    )

@router.message(F.text == "Справка")
async def cmd_how(message: Message):
    await message.answer(
        "Справка: ",
        reply_markup=kb.spravka
    )

@router.callback_query(F.data == "w_skill")
async def cmd_skill(callback: CallbackQuery):
    await callback.answer("ppap")
    await callback.message.answer("Бот создан для того, чтобы напоминать вам о событиях.")

@router.callback_query(F.data == "info")
async def cmd_skill(callback: CallbackQuery):
    await callback.answer("ppap")
    await callback.message.answer("Бот создан как учебный проект.\n Информация об авторе: \n github: https://github.com/k0lttt \n Донат: jopa")

@router.message(F.text == "Поддержка")
async def cmd_help(message: Message):
    await message.answer(
        "Для помощи обратитесь: @132lol321\n*Если столкнулись с проблемой, или нашли ошибку, сообщите в Поддержку!*"
    )
