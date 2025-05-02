
import telebot

# Molly Berry боттың токені
API_TOKEN = '7809160644:AAFmDpx0qvMPm085JrQG3MTe526RaLQvmaI'
bot = telebot.TeleBot(API_TOKEN)

# /start командасы
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Сәлеметсіз бе! Бұл — Molly Berry клубника в шоколаде бот. Тапсырыс беру үшін /order командасын пайдаланыңыз.")

# /order командасы
@bot.message_handler(commands=['order'])
def order(message):
    bot.reply_to(message, 
        "Қанша дана алғыңыз келеді? 🍓\n\n"
        "• 6 дана – 4500 ₸\n"
        "• 9 дана – 5500 ₸\n"
        "• 12 дана – 7500 ₸\n"
        "• 16 дана – 10500 ₸\n"
        "• 20 дана – 12500 ₸\n"
        "• 24 дана – 14500 ₸\n"
        "• 30 дана – 18500 ₸\n"
        "• 48 дана – 33500 ₸\n\n"
        "Тапсырыс беру үшін толық есіміңізді жазыңыз:")

# /help командасы
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, 
        "Қол жетімді командалар:\n\n"
        "/start - Ботты бастау\n"
        "/order - Клубника в шоколаде тапсырыс беру\n"
        "/help - Қол жетімді командалар тізімі\n"
        "/contact - Байланыс мәліметтері\n"
        "/payment - Kaspi арқылы төлем жасау\n"
        "/status - Тапсырыстың күйін тексеру\n"
        "/cancel - Тапсырысты немесе процесс жою\n"
        "/empty - Командалар тізімін босату")

# /contact командасы
@bot.message_handler(commands=['contact'])
def contact(message):
    bot.reply_to(message, 
        "Бізбен байланысу үшін WhatsApp арқылы хабарласыңыз:\n"
        "https://wa.me/message/KCO2ZTHXQJJJA1")

# /payment командасы
@bot.message_handler(commands=['payment'])
def payment(message):
    bot.reply_to(message, 
        "Сіздің тапсырысыңыз қабылданды!\n\n"
        "Төлем үшін Kaspi Gold нөмірі: 87714227805 (Разуан Е.) 📲\n"
        "Төлем жасаған соң чекті жіберуді ұмытпаңыз.\n\n"
        "Күніңіз сәтті болсын! 🍫🍓")

# /status командасы
@bot.message_handler(commands=['status'])
def status(message):
    bot.reply_to(message, 
        "Қазіргі тапсырыстың күйі:\n"
        "• Тапсырыс күтілуде немесе өңделуде\n"
        "• Төлем расталмаған болса, /payment арқылы төлеңіз")

# /cancel командасы
@bot.message_handler(commands=['cancel'])
def cancel(message):
    bot.reply_to(message, 
        "Тапсырысыңыз немесе әрекет жойылды.\nҚайта бастау үшін /order пәрменін қолданыңыз.")

# /empty командасы
@bot.message_handler(commands=['empty'])
def empty(message):
    bot.reply_to(message, "Командалар тізімі босатылды.")

# Ботты іске қосу
bot.polling()
