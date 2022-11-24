
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("5321604006:AAF2ALNg7mBv7_tXZ4fKhQsHtSC8k1aNrHE")

nowsend =0

@bot.message_handler(content_types=['text'])
def handler(message):
    global nowsend
    connect = sqlite3.connect('textDB')
    cursor = connect.cursor()
    cursor.execute(f"SELECT id FROM textDB WHERE id = '{message.chat.id}'")
    data = cursor.fetchone()
    if data is None:
        cursor.execute(f"INSERT INTO textDB VALUES(?,?)", (message.chat.id, None))
        connect.commit()

    if message.from_user.id == 777000:
        bot.reply_to(message,"Правила чату \n 1 ) remember no russian \n 2) Можете сказати нам про помилки , я прочитаю та передам команді ваші слова \n 3) Без спаму \n 4) Пам'ятайте це чат обговорення манги , якщо бажаєте обговорювати політику ласкаво просимо у інші чати \n 5) Не обговорюйте погану якість тих чи інших членів команди ( вони ображаються ) \n На цьому все ! ")
    if message.text == "/start":


        item1 = types.KeyboardButton("📝")
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(item1)

        bot.send_message(message.chat.id, text='Start Work', reply_markup=markup)




    if nowsend == 1:
        cursor.execute(f"UPDATE textDB SET text = '{message.text}' WHERE id = {message.chat.id}")
        connect.commit()
        bot.send_message(message.chat.id,"message saved")
        nowsend = 0

    if  message.text == "/report":

        if message.reply_to_message != None  :
            chat = 't.me/c/1607402725'
            message1 = "https://"+str(chat) + "/" + str(message.id) + " "+ "report від " + message.from_user.username
            bot.send_message(866150895,message1)
            bot.reply_to(message,"Повідомлення відправлено на перевірку")
        else :
            bot.reply_to(message,"будь ласка відправте репорт відповідь на повідомлення на яке ви бажаєте відправити репорт")


    if message.text == "📝":
        bot.send_message(message.chat.id, "send text")
        nowsend = 1

bot.polling(none_stop=True)