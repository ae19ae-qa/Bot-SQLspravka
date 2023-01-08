#библиотеки, которые загружаем из вне
import telebot
TOKEN = 'Мой токен'

from telebot import types

bot = telebot.TeleBot(TOKEN)

#описание внешнего вида бота - до логики -сделать кнопки с названиями
@bot.message_handler(commands=['start'])

def welcome(message):
	sti = open('spravka.png', 'rb')
	bot.send_sticker(message.chat.id, sti)

	#клавиатура
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton("Доступ к данным")
	item2 = types.KeyboardButton("Определение данных")
	item3 = types.KeyboardButton("Манипуляции данными")
	item4 = types.KeyboardButton("Управление транзакциями")
	item5 = types.KeyboardButton("Секретный код в SQL")

	markup.add(item1, item2, item3, item4, item5)

	bot.send_message(message.chat.id, "Привет тебе, {0.first_name}! SQL - это много возможностей!".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

#закладываем логику - назначаем действие для клавиатуры 
@bot.message_handler(content_types=['text'])

#создать функция - команда def, сама функция lalala, действия -если ... то... 
def lalala(message):
	if message.chat.type == 'private':
		if message.text == 'Доступ к данным':
			bot.send_message(message.chat.id, 'Это операторы SQL, предназначенные для определения доступа к данным. С их помощью можно закрыть или открыть для пользователей работу с базой. Такие операторы необходимы, чтобы ограничить кого-либо из сотрудников в доступе к информации или, наоборот, позволить работать с базой новому специалисту.')
		elif message.text == 'Определение данных':
			bot.send_message(message.chat.id, 'Такие операторы SQL используются в тех случаях, когда нужно внести в базу новую таблицу или, напротив, удалить старую.')
		elif message.text == 'Манипуляции данными':
			bot.send_message(message.chat.id, 'Эти операторы меняют наполнение таблиц. Они позволяют изменять значение строк, столбцов и прочих атрибутов.')
		elif message.text == 'Управление транзакциями':
			bot.send_message(message.chat.id, 'Сочетание команд, которые выполняются в определённом алгоритме. Транзакция проведена успешно, если все необходимые команды выполнены пошагово. Если же в какой-либо из них произошёл сбой, то вся операция, включая предыдущие команды, отменяется.')
		elif message.text == 'Секретный код в SQL':
			bot.send_message(message.chat.id, 'Я его не знаю, но ты можешь погуглить, и, может быть, обнаружишь!')
		else:
			bot.send_message(message.chat.id, 'Знание расширяет твои возможности! введи /start')

bot.polling(none_stop=True)



#https://core.telegram.org/bots/api#available-methods
