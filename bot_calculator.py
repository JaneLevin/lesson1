from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import re


def greet_user(bot, update):
    print('Вызван /start')
    print(update)
    bot.sendMessage(update.message.chat_id, text='Давай общаться!')


def talk_to_me(bot, update):
    print(update.message.text)
    bot.sendMessage(update.message.chat_id, update.message.text)


def words_count(bot, update):
    user_words = str.split(update.message.text)
    del user_words[0]
    words_cnt = len(user_words)
    output = ""
    if words_cnt == 0:
        output = "{} слов".format(words_cnt)
    elif words_cnt == 1:
        output = " {} слово".format(words_cnt)
    elif words_cnt <= 4:
        output = "{} слова".format(words_cnt)

    print(output)
    bot.sendMessage(update.message.chat_id, text=output)


def calculate(bot, update):
    user_words = str.split(update.message.text)
    response = ""
    try:
        template = r'(\d+)(\S+)(\d+)='
        res = re.search(template, user_words[1])

        first_number = float(res.group(1))
        action = res.group(2)
        second_number = float(res.group(3))

        if action == '+':
            response = "{}".format(first_number + second_number)
        elif action == '-':
            response = "{}".format(first_number - second_number)
        elif action == '*':
            response = "{}".format(first_number * second_number)
        elif action == '/':
            response = "{}".format(first_number / second_number)
    except Exception:
        response = "Неверный ввод. Введено `{}`, нужно, например: `/calculate 2-3=`".format(update.message.text)

    bot.sendMessage(update.message.chat_id, response)


def show_error(bot, update, error):
    print(error)


def main():
    updater = Updater("314707545:AAFctTT1h3urOlUJuJVG72447SewvYSCSWc")
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler([Filters.text], talk_to_me))
    dp.add_handler(CommandHandler("wordcount", words_count))
    dp.add_handler(CommandHandler("calculate", calculate))
    dp.add_error_handler(show_error)

    updater.start_polling()
    updater.idle()


main()
