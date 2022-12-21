from aiogram import Dispatcher, types
import messages as msg

async def menuList(message:types.Message):
    text, keybord = msg.menu_list(message.from_user.id)
    await message.answer(text, reply_markup=keybord)


async def menuListButton(call:types.CallbackQuery):
    text, keybord = msg.menu_list(call.from_user.id)

    await call.answer()
    await call.message.answer(text, reply_markup=keybord)

def menu(dp: Dispatcher):
    dp.register_message_handler(menuList, commands='menu')
    dp.register_callback_query_handler(menuListButton, text="menu")