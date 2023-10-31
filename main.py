import telebot
from telebot import types
from send_file import SendMessagesReq, SendMessagesVid
import os
import dotenv

dotenv.load_dotenv()
API_TOKEN = os.getenv("API_TOKEN")

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_first_name = str(message.chat.first_name)
    user_last_name = str(message.chat.last_name)
    bot.reply_to(message, f"""\
Assalomu alaykum {user_first_name} {user_last_name}\n\
Botga hush kelibsiz.""")
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item_audio = types.KeyboardButton("Audio🎙")
    item_photo = types.KeyboardButton("Rasm📸")
    item_video = types.KeyboardButton("Video🎞")
    item_file = types.KeyboardButton("File🧾")

    markup.add(item_audio, item_photo, item_video, item_file)
    bot.send_message(message.chat.id, 'Ushbu menyulardan birini tanlang!👇', 
                     reply_markup=markup
    )
        
@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text == "Audio🎙":
        bot.send_message(message.chat.id, "Yuklanmoqda ozgina kuting📥...")
        chats_id = message.chat.id
        sendaudio = SendMessagesReq(API_TOKEN, "https://muzfm.tv/music/2017/mp3/06/M1noR_ft_UZmir_L1GHTDreaM-Songgi_Express.mp3", chats_id, "sendAudio", 'audio')
        sendaudio.send("M1nor_ft_Uzmir_SONGI EXSPRESS")

    elif message.text == "Rasm📸":
        bot.send_message(message.chat.id, "Yuklanmoqda ozgina kuting📥...")
        chats_id = message.chat.id
        sendaudio = SendMessagesReq(API_TOKEN, "https://images.unsplash.com/photo-1554080353-a576cf803bda?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8NHx8cGhvdG98ZW58MHx8MHx8fDA%3D&w=1000&q=80", chats_id, "sendPhoto", 'photo')
        sendaudio.send("Telefoningiz uchun Wallpaper")

    elif message.text == "Video🎞":
        bot.send_message(message.chat.id, "Yuklanmoqda ozgina kuting📥...")
        chats_id = message.chat.id
        try:
            bot.send_message(message.chat.id, "Kechirasiz videoni biroz kechroq yuklaydi. Iltomos biroz kuting⌚️...")
            sendVid = SendMessagesVid(API_TOKEN, "file\\media.mp4", chats_id, "sendVideo", 'video')
            sendVid.sendVideos()
        except Exception as e:
            bot.send_message(message.chat.id, "Error: %s" % e)

    elif message.text == "File🧾":
        bot.send_message(message.chat.id, "Yuklanmoqda ozgina kuting📥...")
        chats_id = message.chat.id
        sendaudio = SendMessagesReq(API_TOKEN, "http://tami.uz/kitob/Python_dasturlash_tili.pdf", chats_id, "sendDocument", 'document')
        sendaudio.send("Python Asoslari kitobi")

bot.infinity_polling()