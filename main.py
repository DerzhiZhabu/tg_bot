from telebot import types
import telebot
import json
import datetime
from random import randint

j_file = open('base.json', 'r')
static = json.load(j_file)

j_file.close()


class Test1:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Толстый(ая)")
        bt2 = types.KeyboardButton("Худой(ая)")
        self.markup.add(bt1, bt2)

    def q(self, id, user):
        pre = static[user]['pre']
        stadia = pre[1] + 1
        if stadia == 1 or 4 <= stadia <= 5 or 8 <= stadia <= 9 or stadia == 11 \
                or stadia == 13 or stadia == 15 or stadia == 18 or stadia == 20:
            self.fat(id, static[user]["exceptions_fat"], user)
        else:
            self.thin(id, static[user]["exceptions_thin"], user)
        if pre[1] == 20:
            static[user]["pre"] = [pre[0] + 1, 0]
        else:
            static[user]["pre"] = [pre[0], pre[1] + 1]

    def fat(self, id, exceptions, user):
        rand = randint(1, 10)
        while rand in exceptions:
            rand = randint(1, 10)
        exceptions.append(rand)
        static[user]["exceptions_fat"] = exceptions.copy()
        g = open(f'./images/fat/fat{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def thin(self, id, exceptions, user):
        rand = randint(1, 10)
        while rand in exceptions:
            rand = randint(1, 10)
        exceptions.append(rand)
        static[user]["exceptions_thin"] = exceptions.copy()
        g = open(f'./images/thin/thin{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()


def save():
    j_file = open('base.json', 'w')
    json.dump(static, j_file)
    j_file.close()


bot = telebot.TeleBot("7117623225:AAEaYEIyAHed3zfh8dYOBTbVuLvaPIlthE0", parse_mode=None)

test1 = Test1()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Я согласен (согласна) и хочу продолжить")
    markup.add(bt1)
    bot.send_message(message.chat.id,
                     "Рады приветствовать вас на “Тестировании скрытой ассоциации (Implicit Association Test (IAT).\n"
                     " Этот бот разработан студентами Новосибирского государственного университета для проекта по психологии.\n"
                     "Мы предлагаем вам пройти тест, который направлен на выявление подсознательных предубеждений по отношению к толстым и худым людям. Главное условие — отвечать на вопросы как можно быстрее.\n"
                     "В ходе выполнения теста вам необходимо честно указать своё ощущение, отношение или убеждение по представленным темам. Также нам понадобится некоторая информация о вас (пол и возраст) в целях формирования обезличенной статистики.\n"
                     "Исследование займет менее 10 минут.", reply_markup=markup)
    static[message.from_user.username] = {"pre": [0, 0]}
    save()


@bot.message_handler(content_types=['text'])
def func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stadia = static[message.from_user.username]["pre"]

    if stadia[0] == 0 and stadia[1] == 0:
        if message.text == "Я согласен (согласна) и хочу продолжить":
            static[message.from_user.username]["pre"] = [0, 1]
            bot.send_message(message.chat.id, "Введите ваш возраст:", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 1:
        if message.text.isdigit():
            static[message.from_user.username]["pre"] = [0, 2]
            static[message.from_user.username]["age"] = int(message.text)
            for i in range(1, 8):
                bt = types.KeyboardButton(str(i))
                markup.add(bt)
            bot.send_message(message.chat.id, "Какое утверждение вам ближе всего? (отвечайте как можно быстрее)\n"
                                              "1) Я предпочитаю толстых людей худым.\n"
                                              "2) Я умеренно предпочитаю толстых людей худым. \n"
                                              "3) Я немного предпочитаю толстых людей худым. \n"
                                              "4) Мне одинаково нравятся толстые и худые люди. \n"
                                              "5) Я немного предпочитаю худых людей толстым. \n"
                                              "6) Я умеренно предпочитаю худых людей толстым.\n"
                                              "7) Я предпочитаю худых людей толстым.\n", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 2:
        if message.text.isdigit():
            if 1 <= int(message.text) <= 7:
                static[message.from_user.username]["pre"] = [0, 3]
                static[message.from_user.username]["predp"] = int(message.text)
                bot.send_message(message.chat.id,
                                 "Оцените (напишите только целое число), как вы относитесь к худым людям по шкале от 0 до 10,"
                                 " если 0 - очень холодно, 10 - очень тепло. (отвечайте как можно быстрее)",
                                 reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 3:
        if message.text.isdigit():
            if 0 <= int(message.text) <= 10:
                static[message.from_user.username]["pre"] = [0, 4]
                static[message.from_user.username]["predp_thin"] = int(message.text)
                bot.send_message(message.chat.id,
                                 "Оцените (напишите только целое число), как вы относитесь к толстым людям по шкале от 0 до 10,"
                                 " если 0 - очень холодно, 10 - очень тепло. (отвечайте как можно быстрее)",
                                 reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 4:
        if message.text.isdigit():
            if 0 <= int(message.text) <= 10:
                static[message.from_user.username]["pre"] = [0, 5]
                static[message.from_user.username]["predp_fat"] = int(message.text)
                bt = types.KeyboardButton("Мужской")
                bt2 = types.KeyboardButton("Женский")
                bt3 = types.KeyboardButton("Боевой вертолет")
                markup.add(bt, bt2, bt3)
                bot.send_message(message.chat.id, "Укажите ваш пол", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 5:
        if message.text == "Мужской" or message.text == "Женский" or message.text == "Боевой вертолет":
            static[message.from_user.username]["pre"] = [0, 6]
            static[message.from_user.username]["gender"] = message.text
            bot.send_message(message.chat.id,
                             "Теперь вам необходимо как можно быстрее распределить элементы по группам.\n"
                             "Ознакомьтесь с четырьмя группами и их элементами на изображении: ", reply_markup=markup)
            bt = types.KeyboardButton("Понятно")
            markup.add(bt)
            g = open("images/main.jpg", "rb")
            bot.send_photo(message.chat.id, g, reply_markup=markup)
            g.close()
            bot.send_message(message.chat.id, "Всего пройдет семь раундов. В раундах могут изменяться инструкции. Будьте внимательны!", reply_markup=markup)

        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 6:
        if message.text == "Понятно":
            static[message.from_user.username]["pre"] = [0, 7]
            bt = types.KeyboardButton("Начать раунд!")
            markup.add(bt)
            bot.send_message(message.chat.id, "Раунд 1/7. Вам будут представлены силуэты толстых и худых людей по одному."
                                              "Нажмите левую кнопку, если перед вами силуэт толстого человека,"
                                              "правую кнопку — если перед вами силуэт худого человека.\n"
                                              "Если вы допустите ошибку и появится красный крестик (❌), то нажмите на другую кнопку."
                                              "Отвечайте как можно быстрее, но старайтесь не ошибаться.", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 7:
        if message.text == "Начать раунд!":
            static[message.from_user.username]["pre"] = [1, 0]
            static[message.from_user.username]["exceptions_fat"] = []
            static[message.from_user.username]["exceptions_thin"] = []
            test1.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 1 and 0 <= stadia[1] < 20:
        if message.text == "Толстый(ая)" or message.text == "Худой(ая)":
            test1.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "А пока все", reply_markup=markup)
    save()


bot.infinity_polling()
