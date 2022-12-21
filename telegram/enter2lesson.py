from aiogram import Dispatcher, types
import messages as msg

async def enter_2_lesson(call:types.CallbackQuery):
    message = msg.enter_lesson(call.from_user.id ,call.data)

    await call.answer()
    await call.message.answer(message)

    text, keybord = msg.menu_list(call.from_user.id)
    await call.message.answer(text, reply_markup=keybord)

def enter2lesson(dp:Dispatcher):
    dp.register_callback_query_handler(enter_2_lesson, lambda call: "enter" in call.data)
