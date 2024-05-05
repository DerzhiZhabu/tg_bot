from telebot import types
import telebot
import json
import datetime
from random import randint

j_file = open('base.json', 'r')
static = json.load(j_file)

j_file.close()


class Test7:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Плохое или Худой")
        bt2 = types.KeyboardButton("Хорошее или Толстый")
        self.markup.add(bt1, bt2)

    def q(self, id, user):
        pre = static[user]['pre']

        flag = True
        while flag:  # 0 - fat, 1 - thin, 2 - bad, 3 - good
            if static[user]["lastt"] == 2 or static[user]["lastt"] == 3:
                r = randint(0, 1)
            else:
                r = randint(2, 3)
            if r == 0:
                rand = randint(1, 10)
                if rand not in static[user]["ex_fat"]:
                    static[user]["ex_fat"].append(rand)
                    self.fat(id, [], user, rand)
                    flag = False
                elif static[user]["povt_fat"] < 0:
                    static[user]["povt_fat"] += 1
                    self.fat(id, [], user, rand)
                    flag = False
            elif r == 1:
                rand = randint(1, 10)
                if rand not in static[user]["ex_thin"]:
                    static[user]["ex_thin"].append(rand)
                    self.thin(id, [], user, rand)
                    flag = False
                elif static[user]["povt_thin"] < 0:
                    static[user]["povt_thin"] += 1
                    self.thin(id, [], user, rand)
                    flag = False
            elif r == 2:
                rand = randint(1, 8)
                if rand not in static[user]["ex_bad"]:
                    static[user]["ex_bad"].append(rand)
                    self.bad(id, [], user, rand)
                    flag = False
                elif static[user]["povt_bad"] < 2:
                    static[user]["povt_bad"] += 1
                    self.bad(id, [], user, rand)
                    flag = False
            elif r == 3:
                rand = randint(1, 8)
                if rand not in static[user]["ex_good"]:
                    static[user]["ex_good"].append(rand)
                    self.good(id, [], user, rand)
                    flag = False
                elif static[user]["povt_good"] < 2:
                    static[user]["povt_good"] += 1
                    self.good(id, [], user, rand)
                    flag = False

        static[user]["lastt"] = r
        static[user]["pre"] = [pre[0], pre[1] + 1]

    def fat(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Толстый"
        g = open(f'./images/fat/fat{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def thin(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Худой"
        g = open(f'./images/thin/thin{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def bad(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Худой"
        g = open(f'./images/bad/bad{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def good(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Толстый"
        g = open(f'./images/good/good{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()


class Test6:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Плохое или Худой")
        bt2 = types.KeyboardButton("Хорошее или Толстый")
        self.markup.add(bt1, bt2)

    def q(self, id, user):
        pre = static[user]['pre']

        flag = True
        while flag:  # 0 - fat, 1 - thin, 2 - bad, 3 - good
            if static[user]["lastt"] == 2 or static[user]["lastt"] == 3:
                r = randint(0, 1)
            else:
                r = randint(2, 3)
            if r == 0 and len(static[user]["ex_fat"]) < 5:
                rand = randint(1, 10)
                if rand not in static[user]["ex_fat"]:
                    static[user]["ex_fat"].append(rand)
                    self.fat(id, [], user, rand)
                    flag = False
            elif r == 1 and len(static[user]["ex_thin"]) < 5:
                rand = randint(1, 10)
                if rand not in static[user]["ex_thin"]:
                    static[user]["ex_thin"].append(rand)
                    self.thin(id, [], user, rand)
                    flag = False
            elif r == 2 and len(static[user]["ex_bad"]) < 5:
                rand = randint(1, 8)
                if rand not in static[user]["ex_bad"]:
                    static[user]["ex_bad"].append(rand)
                    self.bad(id, [], user, rand)
                    flag = False
            elif r == 3 and len(static[user]["ex_good"]) < 5:
                rand = randint(1, 8)
                if rand not in static[user]["ex_good"]:
                    static[user]["ex_good"].append(rand)
                    self.good(id, [], user, rand)
                    flag = False

        static[user]["lastt"] = r

        if pre[1] == 20:
            static[user]["pre"] = [pre[0] + 1, 0]
        else:
            static[user]["pre"] = [pre[0], pre[1] + 1]

    def fat(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Толстый"
        g = open(f'./images/fat/fat{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def thin(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Худой"
        g = open(f'./images/thin/thin{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def bad(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Худой"
        g = open(f'./images/bad/bad{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def good(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Толстый"
        g = open(f'./images/good/good{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()


class Test5:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Худой")
        bt2 = types.KeyboardButton("Толстый")
        self.markup.add(bt1, bt2)

    def q(self, id, user):
        pre = static[user]['pre']

        flag = True
        while flag:
            r = randint(0, 1)
            if r == 0:
                rand = randint(1, 10)
                if rand not in static[user]["ex_fat"]:
                    static[user]["ex_fat"].append(rand)
                    self.fat(id, [], user, rand)
                    flag = False
                elif static[user]["povt_fat"] < 4:
                    static[user]["povt_fat"] += 1
                    self.fat(id, [], user, rand)
                    flag = False
            elif r == 1:
                rand = randint(1, 10)
                if rand not in static[user]["ex_thin"]:
                    static[user]["ex_thin"].append(rand)
                    self.thin(id, [], user, rand)
                    flag = False
                elif static[user]["povt_thin"] < 3:
                    static[user]["povt_thin"] += 1
                    self.thin(id, [], user, rand)
                    flag = False

        static[user]["lastt"] = r
        static[user]["pre"] = [pre[0], pre[1] + 1]

    def fat(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Толстый"
        g = open(f'./images/fat/fat{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def thin(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Худой"
        g = open(f'./images/thin/thin{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def bad(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Толстый"
        g = open(f'./images/bad/bad{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()


class Test4:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Плохое или Толстый")
        bt2 = types.KeyboardButton("Хорошее или Худой")
        self.markup.add(bt1, bt2)

    def q(self, id, user):
        pre = static[user]['pre']

        flag = True
        while flag:  # 0 - fat, 1 - thin, 2 - bad, 3 - good
            if static[user]["lastt"] == 2 or static[user]["lastt"] == 3:
                r = randint(0, 1)
            else:
                r = randint(2, 3)
            print(r)
            if r == 0:
                rand = randint(1, 10)
                if rand not in static[user]["ex_fat"]:
                    static[user]["ex_fat"].append(rand)
                    self.fat(id, [], user, rand)
                    flag = False
                elif static[user]["povt_fat"] < 0:
                    static[user]["povt_fat"] += 1
                    self.fat(id, [], user, rand)
                    flag = False
            elif r == 1:
                rand = randint(1, 10)
                if rand not in static[user]["ex_thin"]:
                    static[user]["ex_thin"].append(rand)
                    self.thin(id, [], user, rand)
                    flag = False
                elif static[user]["povt_thin"] < 0:
                    static[user]["povt_thin"] += 1
                    self.thin(id, [], user, rand)
                    flag = False
            elif r == 2:
                rand = randint(1, 8)
                if rand not in static[user]["ex_bad"]:
                    static[user]["ex_bad"].append(rand)
                    self.bad(id, [], user, rand)
                    flag = False
                elif static[user]["povt_bad"] < 2:
                    static[user]["povt_bad"] += 1
                    self.bad(id, [], user, rand)
                    flag = False
            elif r == 3:
                rand = randint(1, 8)
                if rand not in static[user]["ex_good"]:
                    static[user]["ex_good"].append(rand)
                    self.good(id, [], user, rand)
                    flag = False
                elif static[user]["povt_good"] < 2:
                    static[user]["povt_good"] += 1
                    self.good(id, [], user, rand)
                    flag = False

        static[user]["lastt"] = r
        static[user]["pre"] = [pre[0], pre[1] + 1]
        r = -1

    def fat(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Толстый"
        g = open(f'./images/fat/fat{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def thin(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Худой"
        g = open(f'./images/thin/thin{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def bad(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Толстый"
        g = open(f'./images/bad/bad{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def good(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Худой"
        g = open(f'./images/good/good{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()


class Test3:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Плохое или Толстый")
        bt2 = types.KeyboardButton("Хорошее или Худой")
        self.markup.add(bt1, bt2)

    def q(self, id, user):
        pre = static[user]['pre']
        stadia = pre[1] + 1
        funcc = [self.bad, self.good]
        ex = [static[user]["ex_bad"], static[user]["ex_good"]]

        flag = True
        while flag:  # 0 - fat, 1 - thin, 2 - bad, 3 - good
            if static[user]["lastt"] == 2 or static[user]["lastt"] == 3:
                r = randint(0, 1)
            else:
                r = randint(2, 3)
            if r == 0 and len(static[user]["ex_fat"]) < 5:
                rand = randint(1, 10)
                if rand not in static[user]["ex_fat"]:
                    static[user]["ex_fat"].append(rand)
                    self.fat(id, [], user, rand)
                    flag = False
            elif r == 1 and len(static[user]["ex_thin"]) < 5:
                rand = randint(1, 10)
                if rand not in static[user]["ex_thin"]:
                    static[user]["ex_thin"].append(rand)
                    self.thin(id, [], user, rand)
                    flag = False
            elif r == 2 and len(static[user]["ex_bad"]) < 5:
                rand = randint(1, 8)
                if rand not in static[user]["ex_bad"]:
                    static[user]["ex_bad"].append(rand)
                    self.bad(id, [], user, rand)
                    flag = False
            elif r == 3 and len(static[user]["ex_good"]) < 5:
                rand = randint(1, 8)
                if rand not in static[user]["ex_good"]:
                    static[user]["ex_good"].append(rand)
                    self.good(id, [], user, rand)
                    flag = False

        static[user]["lastt"] = r

        if pre[1] == 20:
            static[user]["pre"] = [pre[0] + 1, 0]
        else:
            static[user]["pre"] = [pre[0], pre[1] + 1]

    def fat(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Толстый"
        g = open(f'./images/fat/fat{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def thin(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Худой"
        g = open(f'./images/thin/thin{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def bad(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое или Толстый"
        g = open(f'./images/bad/bad{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def good(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее или Худой"
        g = open(f'./images/good/good{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()


class Test2:
    def __init__(self):
        self.markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bt1 = types.KeyboardButton("Плохое")
        bt2 = types.KeyboardButton("Хорошее")
        self.markup.add(bt1, bt2)

    def q(self, id, user):
        pre = static[user]['pre']
        stadia = pre[1] + 1
        funcc = [self.bad, self.good]
        ex = [static[user]["ex_bad"], static[user]["ex_good"]]
        povt_good = static[user]["povt_good"]
        povt_bad = static[user]["povt_bad"]

        flag = True
        while flag:
            r = randint(0, 1)
            rand = randint(1, 8)
            if rand not in ex[r]:
                funcc[r](id, [], user, rand)
                flag = False
                if r == 0:
                    static[user]["ex_bad"].append(rand)
                else:
                    static[user]["ex_good"].append(rand)
            else:
                if r == 0 and povt_bad < 2:
                    static[user]["povt_bad"] += 1
                    funcc[r](id, [], user, rand)
                    flag = False
                elif r == 1 and povt_good < 2:
                    static[user]["povt_good"] += 1
                    funcc[r](id, [], user, rand)
                    flag = False
        if pre[1] == 20:
            static[user]["pre"] = [pre[0] + 1, 0]
        else:
            static[user]["pre"] = [pre[0], pre[1] + 1]

    def bad(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Плохое"
        g = open(f'./images/bad/bad{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()

    def good(self, id, exceptions, user, rand):
        static[user]["last_good"] = "Хорошее"
        g = open(f'./images/good/good{rand}.jpg', 'rb')
        bot.send_message(id, "К какой группе относится эта картинка")
        bot.send_photo(id, g, reply_markup=self.markup)
        g.close()


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
        static[user]["last_good"] = "Толстый(ая)"
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
        static[user]["last_good"] = "Худой(ая)"
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
test2 = Test2()
test3 = Test3()
test4 = Test4()
test5 = Test5()
test6 = Test6()
test7 = Test7()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    bt1 = types.KeyboardButton("Я согласен (согласна) и хочу продолжить")
    markup.add(bt1)
    bot.send_message(message.chat.id,
                     "Рады приветствовать вас на “Тестировании скрытой ассоциации (Implicit Association Test (IAT).\n"
                     "Этот бот разработан студентами Новосибирского государственного университета для проекта по психологии.\n"
                     "Мы предлагаем вам пройти тест, который направлен на выявление подсознательных предубеждений по отношению к толстым и худым людям. Главное условие — отвечать на вопросы как можно быстрее.\n"
                     "В ходе выполнения теста вам необходимо честно указать своё ощущение, отношение или убеждение по представленным темам. Также нам понадобится некоторая информация о вас (пол и возраст) в целях формирования обезличенной статистики.\n"
                     "Исследование займет примерно 10 минут.", reply_markup=markup)
    static[message.from_user.username] = {"pre": [0, 0]}
    save()


@bot.message_handler(content_types=['text'])
def func(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    stadia = static[message.from_user.username]["pre"]
    if message.text.lower() == 'иди нахуй':
        bot.send_message(message.chat.id, "Сам иди👍", reply_markup=markup)

    if stadia[0] == 0 and stadia[1] == 0:
        if message.text == "Я согласен (согласна) и хочу продолжить":
            static[message.from_user.username]["pre"] = [0, 1]
            bot.send_message(message.chat.id, "Введите ваш возраст:", reply_markup=types.ReplyKeyboardRemove())

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
                                 reply_markup=types.ReplyKeyboardRemove())
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
                                 reply_markup=types.ReplyKeyboardRemove())
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
            bot.send_message(message.chat.id,
                             "Всего пройдет семь раундов. В раундах могут изменяться инструкции. Будьте внимательны!",
                             reply_markup=markup)

        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 0 and stadia[1] == 6:
        if message.text == "Понятно":
            static[message.from_user.username]["pre"] = [0, 7]
            bt = types.KeyboardButton("Начать раунд!")
            markup.add(bt)
            bot.send_message(message.chat.id,
                             "Раунд 1/7. Вам будут представлены силуэты толстых и худых людей по одному."
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
            if message.text == static[message.from_user.username]["last_good"]:
                test1.q(message.chat.id, message.from_user.username)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 1 and stadia[1] == 20:
        if message.text == "Толстый(ая)" or message.text == "Худой(ая)":
            if message.text == static[message.from_user.username]["last_good"]:
                static[message.from_user.username]["pre"] = [1, 21]
                static[message.from_user.username].pop("exceptions_fat")
                static[message.from_user.username].pop("exceptions_thin")
                static[message.from_user.username]['povt_good'] = 0
                static[message.from_user.username]['povt_bad'] = 0
                static[message.from_user.username]['ex_bad'] = []
                static[message.from_user.username]['ex_good'] = []
                bt = types.KeyboardButton("Начать раунд!")
                markup.add(bt)
                bot.send_message(message.chat.id, "Раунд 2/7. Вам будут представлены «плохие» и «хорошие» слова по одному."
                                                  " Нажмите левую кнопку, если перед вами плохое слово, правую кнопку — если перед вами хорошее слово."
                                                  " Если вы допустите ошибку и появится красный крестик (❌), нажмите на другую кнопку. Отвечайте как можно быстрее, но старайтесь не ошибаться.",
                                 reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 1 and stadia[1] == 21:
        if message.text == "Начать раунд!":
            static[message.from_user.username]["pre"] = [2, 0]
            test2.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 2 and 0 <= stadia[1] < 20:
        if message.text == "Хорошее" or message.text == "Плохое":
            if message.text == static[message.from_user.username]["last_good"]:
                test2.q(message.chat.id, message.from_user.username)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 2 and stadia[1] == 20:
        if message.text == "Хорошее" or message.text == "Плохое":
            if message.text == static[message.from_user.username]["last_good"]:
                static[message.from_user.username]["pre"] = [2, 21]

                static[message.from_user.username].pop('povt_good')
                static[message.from_user.username].pop('povt_bad')
                static[message.from_user.username].pop('ex_bad')
                static[message.from_user.username].pop('ex_good')

                static[message.from_user.username]['ex_bad'] = []
                static[message.from_user.username]['ex_good'] = []
                static[message.from_user.username]['ex_fat'] = []
                static[message.from_user.username]['ex_thin'] = []
                static[message.from_user.username]['last_good'] = ''
                static[message.from_user.username]['lastt'] = 2

                bt = types.KeyboardButton("Начать раунд!")
                markup.add(bt)
                bot.send_message(message.chat.id,
                                 "Раунд 3/7. Вам будут представлены «плохие» и «хорошие» слова и силуэты толстых "
                                 "и худых людей по одному. Нажмите левую кнопку, если перед вами плохое слово или толстый человек, "
                                 "правую кнопку — если перед вами хорошее слово или худой человек.\n"
                                 "Если вы допустите ошибку и появится красный крестик (❌), нажмите на другую кнопку.\n"
                                 "Отвечайте как можно быстрее, но старайтесь не ошибаться.", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 2 and stadia[1] == 21:
        if message.text == "Начать раунд!":
            static[message.from_user.username]["pre"] = [3, 0]
            test3.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 3 and 0 <= stadia[1] < 20:
        if message.text == "Хорошее или Худой" or message.text == "Плохое или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                test3.q(message.chat.id, message.from_user.username)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 3 and stadia[1] == 20:
        if message.text == "Хорошее или Худой" or message.text == "Плохое или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                static[message.from_user.username]["pre"] = [3, 21]

                static[message.from_user.username]['povt_good'] = 0
                static[message.from_user.username]['povt_bad'] = 0
                static[message.from_user.username]['povt_fat'] = 0
                static[message.from_user.username]['povt_thin'] = 0

                static[message.from_user.username]['ex_bad'] = []
                static[message.from_user.username]['ex_good'] = []
                static[message.from_user.username]['ex_fat'] = []
                static[message.from_user.username]['ex_thin'] = []
                static[message.from_user.username]['last_good'] = ''
                static[message.from_user.username]['lastt'] = 2

                bt = types.KeyboardButton("Начать раунд!")
                markup.add(bt)
                bot.send_message(message.chat.id,
                                 "Раунд 4/7. Вам будут представлены «плохие» и «хорошие» слова и силуэты толстых и худых людей по одному. "
                                 "Нажмите левую кнопку, если перед вами плохое слово или толстый человек, правую кнопку — если перед вами хорошее слово или худой человек.\n"
                                 "Если вы допустите ошибку и появится красный крестик (❌), нажмите на другую кнопку.\n"
                                 "Отвечайте как можно быстрее, но старайтесь не ошибаться.", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 3 and stadia[1] == 21:
        if message.text == "Начать раунд!":
            static[message.from_user.username]["pre"] = [4, 0]
            test4.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 4 and 0 <= stadia[1] < 40:
        if message.text == "Хорошее или Худой" or message.text == "Плохое или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                test4.q(message.chat.id, message.from_user.username)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 4 and stadia[1] == 40:
        if message.text == "Хорошее или Худой" or message.text == "Плохое или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                static[message.from_user.username]["pre"] = [4, 41]

                static[message.from_user.username]['povt_good'] = 0
                static[message.from_user.username]['povt_bad'] = 0
                static[message.from_user.username]['povt_fat'] = 0
                static[message.from_user.username]['povt_thin'] = 0

                static[message.from_user.username]['ex_bad'] = []
                static[message.from_user.username]['ex_good'] = []
                static[message.from_user.username]['ex_fat'] = []
                static[message.from_user.username]['ex_thin'] = []
                static[message.from_user.username]['last_good'] = ''
                static[message.from_user.username]['lastt'] = 2

                bt = types.KeyboardButton("Начать раунд!")
                markup.add(bt)
                bot.send_message(message.chat.id,
                                 "Раунд 5/7.Вам будут представлены силуэты худых и толстых людей по одному. "
                                 "Нажмите левую кнопку, если перед вами силуэт худого человека, правую кнопку — если перед вами силуэт толстого человека.\n"
                                 "Если вы допустите ошибку, появится красный крестик (❌), нажмите на другую кнопку. \n"
                                 "Отвечайте как можно быстрее, но старайтесь не ошибаться.", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 4 and stadia[1] == 41:
        if message.text == "Начать раунд!":
            static[message.from_user.username]["pre"] = [5, 0]
            test5.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 5 and 0 <= stadia[1] < 27:
        if message.text == "Худой" or message.text == "Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                test5.q(message.chat.id, message.from_user.username)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 5 and stadia[1] == 27:
        if message.text == "Худой" or message.text == "Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                static[message.from_user.username]["pre"] = [5, 28]

                static[message.from_user.username]['povt_good'] = 0
                static[message.from_user.username]['povt_bad'] = 0
                static[message.from_user.username]['povt_fat'] = 0
                static[message.from_user.username]['povt_thin'] = 0

                static[message.from_user.username]['ex_bad'] = []
                static[message.from_user.username]['ex_good'] = []
                static[message.from_user.username]['ex_fat'] = []
                static[message.from_user.username]['ex_thin'] = []
                static[message.from_user.username]['last_good'] = ''
                static[message.from_user.username]['lastt'] = 2

                bt = types.KeyboardButton("Начать раунд!")
                markup.add(bt)
                bot.send_message(message.chat.id,
                                 "Раунд 6/7. Вам будут представлены «плохие» и «хорошие» слова и силуэты худых  и толстых людей по одному. "
                                 "Нажмите левую кнопку, если перед вами плохое слово или худой человек, правую кнопку — если перед вами хорошее слово или толстый человек.\n"
                                 "Если вы допустите ошибку, появится красный крестик (❌), нажмите на другую кнопку.\n"
                                 "Отвечайте как можно быстрее, но старайтесь не ошибаться.", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 5 and stadia[1] == 28:
        if message.text == "Начать раунд!":
            static[message.from_user.username]["pre"] = [6, 0]
            test6.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 6 and 0 <= stadia[1] < 20:
        if message.text == "Плохое или Худой" or message.text == "Хорошее или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                test6.q(message.chat.id, message.from_user.username)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 6 and stadia[1] == 20:
        if message.text == "Плохое или Худой" or message.text == "Хорошее или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                static[message.from_user.username]["pre"] = [6, 21]

                static[message.from_user.username]['povt_good'] = 0
                static[message.from_user.username]['povt_bad'] = 0
                static[message.from_user.username]['povt_fat'] = 0
                static[message.from_user.username]['povt_thin'] = 0

                static[message.from_user.username]['ex_bad'] = []
                static[message.from_user.username]['ex_good'] = []
                static[message.from_user.username]['ex_fat'] = []
                static[message.from_user.username]['ex_thin'] = []
                static[message.from_user.username]['last_good'] = ''
                static[message.from_user.username]['lastt'] = 2

                bt = types.KeyboardButton("Начать раунд!")
                markup.add(bt)
                bot.send_message(message.chat.id,
                                 "Раунд 7/7. Вам будут представлены «плохие» и «хорошие» слова и силуэты толстых и "
                                 "худых людей по одному. Нажмите левую кнопку, если перед вами плохое слово или худой человек, "
                                 "правую кнопку — если перед вами хорошее слово или толстый человек.\n"
                                 "Если вы допустите ошибку, появится красный крестик (❌), нажмите на другую кнопку.\n"
                                 "Отвечайте как можно быстрее, но старайтесь не ошибаться.", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 6 and stadia[1] == 21:
        if message.text == "Начать раунд!":
            static[message.from_user.username]["pre"] = [7, 0]
            test7.q(message.chat.id, message.from_user.username)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 7 and 0 <= stadia[1] < 40:
        if message.text == "Плохое или Худой" or message.text == "Хорошее или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                test7.q(message.chat.id, message.from_user.username)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    elif stadia[0] == 7 and stadia[1] == 41:
        if message.text == "Плохое или Худой" or message.text == "Хорошее или Толстый":
            if message.text == static[message.from_user.username]["last_good"]:
                static[message.from_user.username]["pre"] = [8, 0]
                bot.send_message(message.chat.id, "Тут типо результат, потом что-нибудь еще, стикеры там. А пока фантазируй.", reply_markup=markup)
            else:
                bot.send_message(message.chat.id, "❌", reply_markup=markup)
        else:
            bot.send_message(message.chat.id, "Не корректный ввод, попробуйте еще раз.", reply_markup=markup)

    else:
        bot.send_message(message.chat.id, "Тут типо результат, потом что-нибудь еще, стикеры там. А пока фантазируй.", reply_markup=markup)

    save()


bot.infinity_polling()
