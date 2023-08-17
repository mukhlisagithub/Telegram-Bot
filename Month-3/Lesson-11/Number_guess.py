from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler
from telegram.ext.filters import TEXT
from telegram import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
from dotenv import load_dotenv
import os


load_dotenv()


btn1 = KeyboardButton(text='Share my Contact', request_contact=True)
btn2 = KeyboardButton(text='Share my Location', request_location=True)
btn3 = KeyboardButton(text='Guess the number')
kb1 = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btn1, btn2], [btn3]], one_time_keyboard=True)

btn2_1 = KeyboardButton(text='Yes')
btn2_2 = KeyboardButton(text='No')
kb2 = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[[btn2_1, btn2_2]])


Left, Right, Number = 0, 100, 50

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) ->None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}', reply_markup=kb1)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text(f'Salom {update.effective_user.first_name}')

async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    global Number, Left, Right
    if text == "Guees the number":
        Left, Right, Number = 0, 100, 50
        await update.message.reply_text('Lets think one number between 1 to 100!', reply_markup=kb2)
        await update.message.reply_text('Is the number greater than 50?')
    elif text in ['Yes', 'No']:
        if text == 'Yes':
            Left, Number = Number + 1, (Number + Right) // 2
        else:
            Right, Number = Number, (Number + Left) // 2
        if Left == Right:
            await update.message.reply_text(f'You number is {Left}', reply_markup=kb1)
        else:
            await update.message.reply_text(f'is the number greater than {Number}?', reply_markup=kb2)
    else:
        await update.message.reply_text(f'Salom')


app = ApplicationBuilder().token(os.getenv('BOT_TOKEN')).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("Hello", hello))
app.add_handler(MessageHandler(TEXT, help))

app.run_polling()
