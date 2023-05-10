from run import Mr_Butler, bot
from aiogram.types import message
from keyboards.reply_keyboards import reply_kb

@Mr_Butler.message_handler(commands=['start'])
async def hi(message: message):
    await bot.send_photo(message.from_user.id,
                         photo='https://s14.stc.yc.kpcdn.net/share/i/3/3033122/wr-750.jpg',
                         caption=f'Привет, дорогой друг!🖖\n'
                                 'Я бот-дворецкий 🤵‍♂️ его величества Сергея Колбасина-младшего.🫅\n'
                                 'Я пока на стадии разработки, поэтому даже здороваться пока сложновато.\n'
                                 'Ходят слухи 👀 что у моего господина родилась дочка 👶, поэтому он редко выходит на связь\n'
                                 'Так что теперь я за него 🤷‍♂\n'
                                 'Но Вы не переживайте!!! Это не надолго, всего лет на 5-10😉\n'
                                 'А пока Вы можете пообщаться со мной, потыкав на клавиатуру-помощник!😇',
                         reply_markup=reply_kb
                                 )