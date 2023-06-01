from run import Mr_Butler, bot
from aiogram.types import message
from keyboards.inline_keyboards import inline_kb3
from datetime import date
from utils.date_transformation import transformation_date
from utils.day_transformation import day_transformation


birthday = date(2023, 4, 25)
current_day = date.today()
difference = (current_day - birthday).days

@Mr_Butler.message_handler(lambda message: 'born' in message.text)
async def hi(message: message):
    await bot.send_photo(message.from_user.id,
                         photo=open('foto/baby.jpg', 'rb'),
                         caption=f'Родилась девочка!\n'
                                 f'Звать <b>Алина</b> 👶\n'
                                 f'Сегодня {transformation_date(str(current_day))}, а значит Алине сейчас {day_transformation(difference)}🥳',
                         reply_markup=inline_kb3, parse_mode='html')