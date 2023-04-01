import pymongo
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove

from dicts import datas as d, text_answer as txt
from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor

bot = Bot(token='5809889690:AAF9avFhpI_pqL5HqxVYbxGpJthMTbnGMVg')

chat_id_admin = 1212069407

dp = Dispatcher(bot)
client = pymongo.MongoClient("mongodb+srv://bot:JXzRunBCX68Ac4MT@biology.mr7dsze.mongodb.net/?retryWrites=true&w=majority")
db = client.user.test


from aiogram import types
from aiogram.dispatcher.filters import BoundFilter


class IsAdmin(BoundFilter):
    async def check(self, msg: types.Message) -> bool:
        return msg.from_user.id == chat_id_admin

class IsUser(BoundFilter):
    async def check(self, msg: types.Message) -> bool:
        return True if db.find_one({'_id': msg.from_user.id}) != None else False

    async def chek_gotovo(self, msg: types.Message) -> bool:
        try:
            return db.find_one({'_id': msg.from_user.id})['gotovo']
        except:
            return False



@dp.message_handler(commands=['start']) # Только старт
async def get_message(msg: types.Message):
    if await IsUser().chek_gotovo(msg):
        await msg.answer(txt['start']['no'])
    elif await IsUser().check(msg):
        await msg.answer(text=txt['start']['nono'])
    else:
        keyboard = types.ReplyKeyboardMarkup(row_width=1)
        keyboard.add(types.KeyboardButton(text=txt['start']['menu'], request_contact=True))
        await msg.answer(text=txt['start']['da'],
                         reply_markup=keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(msg: types.Message):
    if await IsUser().check(msg):
        return None
    else:
        if msg.from_user.id == msg.contact.user_id:
            contact = {
                '_id': msg.from_user.id,
                'username': msg.from_user.username,
                'name': msg.from_user.first_name,
                'Admin': False,
                'msg_id_info': msg.message_id,
                'gotovo': False,
                'result': 0,
                'phone': msg.contact.phone_number
            }
            db.insert_one(contact)
            await msg.answer(txt['contact_save'], reply_markup=ReplyKeyboardRemove())




@dp.message_handler(IsUser(), commands=['test'])
async def test(msg: types.Message):
    if await IsUser().chek_gotovo(msg):
        await msg.answer(txt['test']['no'])
    else:
        db.update_one({'_id': msg.from_user.id}, {'$set': {'result': 0}})
        vopr = d[0]['vopr']
        vstop = txt['test']['vstup']
        text = f'{vstop}\n\n{vopr}'

        menu = InlineKeyboardMarkup()
        menu.add(
            InlineKeyboardButton(text=txt['test']['1'], callback_data=f'vopr_0_1'),
            InlineKeyboardButton(text=txt['test']['2'], callback_data=f'vopr_0_2'))

        await msg.reply(text=text, reply_markup=menu)



@dp.callback_query_handler(Text(startswith='vopr'))
async def while_vopros(callback: types.CallbackQuery):
    vopr = int(callback.data.split('_')[1])
    vibor = int(callback.data.split('_')[2])
    otvet = d[vopr]['otvet']


    try:
        if vibor == otvet:
            user_result = db.find_one({'_id': callback.from_user.id})['result']
            result = user_result + 1
            db.update_one({'_id': callback.from_user.id}, {'$set': {'result': result}})

        new_number_vopros = vopr + 1
        new_vopr = d[new_number_vopros]['vopr']
        vstop = txt['test']['vstup']
        text = f'{vstop}\n\n{new_vopr}'

        menu = InlineKeyboardMarkup()
        menu.add(
            InlineKeyboardButton(text=txt['test']['1'], callback_data=f'vopr_{vopr + 1}_1'),
            InlineKeyboardButton(text=txt['test']['2'], callback_data=f'vopr_{vopr + 1}_2'))
        await callback.answer(txt['test']['answer'])
    except IndexError:
        user_data = db.find_one({'_id': callback.from_user.id})
        result = user_data['result']
        text = txt['test']['result']

        user_username = user_data['username']
        user_name = user_data['name']
        count_vopros = 0
        user_phone = user_data['phone']
        message_id_info = user_data['msg_id_info']
        for i in d:
            count_vopros += 1
        text_admin = f'💬 Клиент @{user_username} прошёл тестирование.\n\n{"="*5} Результаты {"="*5}\n🔸 Имя: {user_name}' \
                     f'\n📝 Результат: {result}/{count_vopros}' \
                     f'\n📞 Номер телефона: {user_phone}\n\n' \
                     f'📍 Кантакты пользователя:'
        await bot.send_message(chat_id=chat_id_admin, text=text_admin)
        await bot.forward_message(chat_id=chat_id_admin, from_chat_id=callback.from_user.id, message_id=message_id_info, disable_notification=True)
        menu = None
        db.update_one({'_id': callback.from_user.id}, {'$set': {'gotovo': True}})
    finally:
        await callback.message.edit_text(text=text, reply_markup=menu)


@dp.message_handler(IsAdmin(), commands=['delete']) # Только старт
async def get_message(msg: types.Message):
    arg = msg.get_args()
    if arg == None:
        await msg.reply('! Команда удаляет все данные о пользователе из БД. \n\nПример: /delete @Zevsuus')
    else:
        arg = arg.replace('@', '')
        db.delete_one({'username': arg})
        await msg.answer('Пользователь удалён из БД!')

@dp.message_handler(IsAdmin(), commands=['reset']) # Только старт
async def get_message(msg: types.Message):
    arg = msg.get_args()
    if arg == None:
        await msg.reply('! Команда позволяет пользователю ещё раз пройти тест. По возможности льзователь будет оповещён. '
                        '\n\nПример: /reset @Zevsuus')
    else:
        arg = arg.replace('@', '')
        user_data = db.find_one({'username': arg})
        if user_data is not None:
            user_id = user_data['_id']
            db.update_one({'_id': user_id}, {'$set': {'gotovo': False}})
            await bot.send_message(chat_id=user_id, text=txt['reset'])
            await msg.answer('Пользователь может снова пройти тест!')
        else:
            await msg.answer('Пользователя нету в БД')


executor.start_polling(dp)

