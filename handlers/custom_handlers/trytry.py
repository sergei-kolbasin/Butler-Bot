from run import Mr_Butler, bot
from aiogram.types import message

@Mr_Butler.message_handler(commands=['🔅'])
async def func(message: message):
    await bot.send_message(message.from_user.id, f'Привет, дорогой друг!🖖\n'
                                 'Я бот-дворецкий его величества Сергея Колбасина-младшего.\n'
                                 'Я пока на стадии разработки, поэтому даже здороваться пока сложновато.\n'
                                 'Но что-то я уже умею делать, к пример вот это /try '
                                 'Ходят слухи 👀 что у моего господина родилась дочка 👶, поэтому он редко выходит на связь\n'
                                 ' '
                                 'появился ')
