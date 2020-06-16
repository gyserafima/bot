from typing import Union, List
import os
import flask
import telebot

from pandas import DataFrame, Series

import conf
import string
import random
import pandas as pd
from collections import Counter

table: Union[Series, None, DataFrame] = pd.read_csv('table3.csv', sep='\t').fillna('')

telebot.apihelper.proxy = conf.PROXY
bot = telebot.TeleBot(conf.TOKEN)

app = flask.Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    sheet = []
    for i in range(0, 2359, 10):
        sheet.append(i)
    global x
    x = random.choice(sheet)
    global base
    base = []
    sent = bot.send_message(message.chat.id, 'Здравствуйте! Напишите что-нибудь, если готовы играть.')
    bot.register_next_step_handler(sent, start_play)


def start_play(message):
    y = 'Вопрос 1: ' + table['question'][x][10:]
    msg = bot.send_message(message.chat.id, y)
    bot.register_next_step_handler(msg, answer_1)


def answer_1(message):
    exclude = set(string.punctuation)
    new_answer = ''.join(ch for ch in table['answer'][x] if ch not in exclude)
    if 'Ответ' in new_answer:
        if message.text.lower() in table['answer'][x].lower() or message.text.lower() in new_answer[6:].lower():
            sent3 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent3, question_2)
        else:
            v = table['answer'][x][6:]
            sent4 = bot.send_message(message.chat.id,
                                     'Правильный ответ:' + v + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent4, question_2)
    else:
        if message.text.lower() == table['answer'][x].lower() or message.text.lower() in new_answer.lower():
            sent3 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent3, question_2)
        else:
            w = table['answer'][x]
            sent4 = bot.send_message(message.chat.id,
                                     'Правильный ответ:' + w + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent4, question_2)


def question_2(message):
    y = 'Вопрос 2: ' + table['question'][x + 1][10:]
    msg = bot.send_message(message.chat.id, y)
    bot.register_next_step_handler(msg, answer_2)


def answer_2(message):
    exclude = set(string.punctuation)
    new_answer = ''.join(ch for ch in table['answer'][x + 1] if ch not in exclude)
    if 'Ответ' in new_answer:
        if message.text.lower() in table['answer'][x + 1].lower() or message.text.lower() in new_answer[6:].lower():
            sent5 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent5, question_3)
        else:
            t = table['answer'][x + 1][6:]
            sent6 = bot.send_message(message.chat.id,
                                     'Правильный ответ:' + t + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent6, question_3)
    else:
        if message.text.lower() == table['answer'][x + 1].lower() or message.text.lower() in new_answer.lower():
            sent5 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent5, question_3)
        else:
            p = table['answer'][x + 1]
            sent6 = bot.send_message(message.chat.id,
                                     'Правильный ответ:' + p + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent6, question_3)


def question_3(message):
    y = 'Вопрос 3: ' + table['question'][x + 2][10:]
    msg = bot.send_message(message.chat.id, y)
    bot.register_next_step_handler(msg, answer_3)


def answer_3(message):
    exclude = set(string.punctuation)
    new_answer = ''.join(ch for ch in table['answer'][x + 2] if ch not in exclude)
    if 'Ответ' in new_answer:
        if message.text.lower() in table['answer'][x + 2].lower() or message.text.lower() in new_answer[6:].lower():
            sent7 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent7, question_4)
        else:
            m = table['answer'][x + 2][6:]
            sent8 = bot.send_message(message.chat.id,
                                     'Правильный ответ:' + m + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent8, question_4)
    else:
        if message.text.lower() == table['answer'][x + 2].lower() or message.text.lower() in new_answer.lower():
            sent7 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent7, question_4)
        else:
            f = table['answer'][x + 2]
            sent8 = bot.send_message(message.chat.id,
                                     'Правильный ответ:' + f + '\n' + 'Напишите что-нибудь, если готовы к следующему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent8, question_4)


def question_4(message):
    y = 'Вопрос 4: ' + table['question'][x + 3][10:]
    msg = bot.send_message(message.chat.id, y)
    bot.register_next_step_handler(msg, answer_4)


def answer_4(message):
    exclude = set(string.punctuation)
    new_answer = ''.join(ch for ch in table['answer'][x + 3] if ch not in exclude)
    if 'Ответ' in new_answer:
        if message.text.lower() in table['answer'][x + 3].lower() or message.text.lower() in new_answer[6:].lower():
            sent9 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к последнему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent9, question_5)
        else:
            g = table['answer'][x + 3][6:]
            sent10 = bot.send_message(message.chat.id,
                                      'Правильный ответ:' + g + '\n' + 'Напишите что-нибудь, если готовы к последнему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent10, question_5)
    else:
        if message.text.lower() == table['answer'][x + 3].lower() or message.text.lower() in new_answer.lower():
            sent9 = bot.send_message(message.chat.id,
                                     'Молодец!' + '\n' + 'Напишите что-нибудь, если готовы к последнему вопросу.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent9, question_5)
        else:
            k = table['answer'][x + 3]
            sent10 = bot.send_message(message.chat.id,
                                      'Правильный ответ:' + k + '\n' + 'Напишите что-нибудь, если готовы к последнему вопросу.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent10, question_5)


def question_5(message):
    y = 'Вопрос 5: ' + table['question'][x + 4][10:]
    msg = bot.send_message(message.chat.id, y)
    bot.register_next_step_handler(msg, answer_5)


def answer_5(message):
    exclude = set(string.punctuation)
    new_answer = ''.join(ch for ch in table['answer'][x + 4] if ch not in exclude)
    if 'Ответ' in new_answer:
        if message.text.lower() in table['answer'][x + 4].lower() or message.text.lower() in new_answer[6:].lower():
            sent11 = bot.send_message(message.chat.id, 'Молодец!' + '\n' + 'Напишите что-нибудь, чтобы закончить игру.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent11, end)
        else:
            z = table['answer'][x + 4][6:]
            sent12 = bot.send_message(message.chat.id,
                                      'Правильный ответ:' + z + '\n' + 'Напишите что-нибудь, чтобы закончить игру.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent12, end)
    else:
        if message.text.lower() == table['answer'][x + 4].lower() or message.text.lower() in new_answer.lower():
            sent11 = bot.send_message(message.chat.id, 'Молодец!' + '\n' + 'Напишите что-нибудь, чтобы закончить игру.')
            base.append('Верных ответов')
            bot.register_next_step_handler(sent11, end)
        else:
            d = table['answer'][x + 4]
            sent12 = bot.send_message(message.chat.id,
                                      'Правильный ответ:' + d + '\n' + 'Напишите что-нибудь, чтобы закончить игру.')
            base.append('Неверных ответов')
            bot.register_next_step_handler(sent12, end)


def end(message):
    sent0 = bot.send_message(message.chat.id, 'Спасибо за игру!' + '\n' + str(Counter(base).most_common(5)) + '\n' + 'Нажмите /start, чтобы сыграть еще.')
    bot.register_next_step_handler(sent0, bot.message_handler)

@app.route("/", methods=['GET', 'HEAD'])
def index():
    return 'ok'

# страница для нашего бота
@app.route("/bot", methods=['POST'])
def webhook():
    if flask.request.headers.get('content-type') == 'application/json':
        json_string = flask.request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        flask.abort(403)

if __name__ == '__main__':
    bot.polling(none_stop=True)