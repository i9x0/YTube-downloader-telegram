from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
from pytube import YouTube
import os
import datetime
updater = Updater("Token Here",use_context=True)
#test test test
try:
 def start(update: Update, context: CallbackContext): 
    x= update.message.text
    user = update.message.from_user.username
    id = update.message.from_user.id
  
    update.message.reply_text(f'hi {user} your id is {id}')
    update.message.reply_text(" ارسل رابط يوتيوب")
    time=datetime.datetime.now()
    file = open('info.txt', 'a')
    file.write("Time:"+str(time)+"\n")
    file.write("username:"+str(user)+"\n")
    file.write("ID:"+str(id)+"\n")
    file.write("Massage:"+x+"\n")

    file.close()
 def unknown(update: Update, context: CallbackContext):
    time=datetime.datetime.now()
    id = update.message.from_user.id
    link = update.message.text
    user = update.message.from_user.username
    file = open('info.txt', 'a')
    file.write("Time:"+str(time)+"\n")
    file.write("username:" +str(user)+"\n")
    file.write("ID:"+str(id)+"\n")
    file.write("link:"+link+"\n")
    file.close()
    update.message.reply_text("انتظر ...")
    try:
     youtubeObject = YouTube(link)
     youtubeObject = youtubeObject.streams.get_lowest_resolution()
    
     x=youtubeObject.download() 
    
     context.bot.send_video(chat_id=update.message.chat_id, video=open(x, 'rb'), supports_streaming=True)
     os.remove(x)
    except:
        update.message.reply_text("الرابط الي بقوائم التشغيل أحيانا ما يحمل ارسل رابط المقطع مباشر")
        print("An error has occurred")

 updater.dispatcher.add_handler(CommandHandler('start', start))
 updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
 updater.start_polling()
except:
    print("tryagain")

