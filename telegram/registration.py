from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
import messages as msg
import database as db
from state import Registration 
import periphery as pr

async def start(message:types.Message):
    text = msg.start(message.from_user.id)
    await message.answer(text)

    #!
    if(not db.UserControll().exist(telegram_id=message.from_user.id)):
        await Registration.first_name.set()
    #!
        await message.answer(pr.what_1name)

async def first_name(message:types.Message, state: FSMContext):
    if(len(message.text)<2):
        await message.answer(pr.what_first_name)
        return
      
    async with state.proxy() as user_data:
        user_data["user"] = db.User()
        user_data["user"].first_name = message.text
        user_data["user"].telegram_id = message.from_user.id
    
    await Registration.next()
    await message.answer(pr.what_0name)

async def last_name(message:types.Message, state: FSMContext):
    if(len(message.text)<2):
        await message.answer(pr.what_last_name)
        return

    async with state.proxy() as user_data:
        user_data["user"].last_name = message.text

    await Registration.next()
    await message.answer(pr.what_group)

async def group(message:types.Message, state: FSMContext):

    if(len(message.text)!=11 and '-' not in message.text):
        await message.answer(pr.wrong_group)
        return

    #!
    group_num, group_id = message.text.split('-')
    async with state.proxy() as user_data:
        user_data["user"].group_num = int(group_num)
        user_data["user"].group_id = db.groupFindId(int(group_id))
        db.UserControll().add(user_data["user"])

    await Registration.next()
    await message.answer(pr.nice_recistration)
    await state.finish()

    text, keybord = msg.menu_list(message.from_user.id)
    await message.answer(text, reply_markup=keybord)

def registration(dp: Dispatcher):
    dp.register_message_handler(start, commands='start')
    dp.register_message_handler(first_name, state=Registration.first_name)
    dp.register_message_handler(last_name, state=Registration.last_name)
    dp.register_message_handler(group, state=Registration.group)


    