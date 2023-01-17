import types

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
# Создаём переменную бота
bot = Bot(token='5809889690:AAF9avFhpI_pqL5HqxVYbxGpJthMTbnGMVg')

# Создаём деспетчер
dp = Dispatcher(bot)



@dp.message_handler(commands=['start']) # Только старт
async def get_message(message: types.Message):

    chat_id = message.chat.id



    chat_id = message.chat.id
    text = f'Здравствуйте, {message.from_user.full_name}! Предлагаю Вам, пройти небольшой опрос. Нажимайте /test если Вы готовы продолжить!'

    await bot.send_message(chat_id=chat_id, text=text)


executor.start_polling(dp)


