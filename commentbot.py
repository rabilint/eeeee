
import telebot


bot = telebot.TeleBot("5324158918:AAHJZsNow4QIiVEklPwtbj0EM5lSeEC-zlw")

@bot.message_handler(content_types=['text'])
def handler(message):
    #bot.send_message(866150895,message)
    if message.from_user.id == 777000:
        bot.reply_to(message,"Правила чату \n 1 ) remember no russian \n 2) Можете сказати нам про помилки , я прочитаю та передам команді ваші слова \n 3) Без спаму \n 4) Пам'ятайте це чат обговорення манги , якщо бажаєте обговорювати політику ласкаво просимо у інші чати \n 5) Не обговорюйте погану якість тих чи інших членів команди ( вони ображаються ) \n На цьому все ! ")
    if  message.text == "/report":
        if message.reply_to_message != None  :
            #chat = bot.get_chat('@channelusername')
            chat = 't.me/c/1607402725'
            message1 = "https://"+str(chat) + "/" + str(message.id) + " "+ "report від " + message.from_user.username
            #bot.forward_message(866150895,-1001607402725, message_id)
            bot.send_message(866150895,message1)
            bot.reply_to(message,"Повідомлення відправлено на перевірку")
        else :
            bot.reply_to(message,"будь ласка відправте репорт відповідь на повідомлення на яке ви бажаєте відправити репорт")


bot.polling(none_stop=True)