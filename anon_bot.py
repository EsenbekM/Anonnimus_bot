from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.types import message, user
from aiogram.utils import executor



bot = Bot(token='2046739731:AAHiTbqnWQwmfKFmQEsGHLoEtvoN4-MZZtY')
dp = Dispatcher(bot)

users=set()

'''*************************************_CLIENT_PART_*****************************************************'''
@dp.message_handler(commands=['how_many'])
async def command_how_many(messege: types.Message):
    await bot.send_message(messege.from_user.id, f"В анонимной группе {len(users)} участников")

@dp.message_handler()
async def send_messege(messege: types.Message):

    for user in users:
        if user != messege.from_user.id:
            await bot.send_message(user, messege.text)
            # await bot.send_photo(chat_id=messege.from_user.id, photo=open(messege.photo, 'rb'))
    users.add(messege.from_user.id)

@dp.message_handler(content_types=['photo'])
async def send_photo(messege):

    for user in users:
        if user != messege.from_user.id:
            await bot.send_photo(user, messege.photo[0].file_id)

    users.add(messege.from_user.id)


@dp.message_handler(content_types=['document'])
async def send_document(messege):
    for user in users:
        if user != messege.from_user.id:
            await bot.send_document(user, messege.document.file_id)

    users.add(messege.from_user.id)
    

#Для аудио
@dp.message_handler(content_types=['audio'])
async def send_audio(messege):
    for user in users:
        if user != messege.from_user.id:
            await bot.send_audio(user ,messege.audio.file_id)

    users.add(messege.from_user.id)

@dp.message_handler(content_types=['voice'])
async def send_voice(messege):
    for user in users:
        if user != messege.from_user.id:
            await bot.send_voice(user, messege.voice.file_id)
        
    users.add(messege.from_user.id)

@dp.message_handler(content_types=['sticker'])
async def send_sticker(messege):
    for user in users:
        if user != messege.from_user.id:
            await bot.send_sticker(user, messege.sticker.file_id)
        
    users.add(messege.from_user.id)

@dp.message_handler(content_types=['video'])
async def send_video(messege):
    for user in users:
        if user != messege.from_user.id:
            await bot.send_video(user, messege.video.file_id)
        
    users.add(messege.from_user.id)

@dp.message_handler(content_types=['video_note'])
async def send_video_note(messege):
    for user in users:
        if user != messege.from_user.id:
            await bot.send_video_note(user, messege.video_note.file_id)
        
    users.add(messege.from_user.id)

executor.start_polling(dp, skip_updates=True)