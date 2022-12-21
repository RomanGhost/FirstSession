from aiogram import Dispatcher, types
import messages as msg

async def lookLesson(call:types.CallbackQuery):
    message, keyboard = msg.look_lesson(call.data)
    await call.answer()
    await call.message.answer(message, reply_markup=keyboard)

def look_lesson(dp:Dispatcher):
    dp.register_callback_query_handler(lookLesson, lambda call: "lesson" in call.data)