import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from telegram.error import TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError
import logging

### initialize bot and logging for debugging ###
bot = telegram.Bot(token=" TOKEN HERE ")
updater = Updater(token=" TOKEN HERE ")
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def error(bot, update, error):
    logger.warning('Update "%s" caused error "%s"' % (update, error))

# start text
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hi. I do a bunch of misc shit. Add me to a group I guess")


start_handler = CommandHandler("start", start)
updater.dispatcher.add_handler(start_handler)


# help command
def helpme(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="Available commands:\n/add x y - adds two numbers\n/subtract x y - subtracts two numbers (x - y)\n/multiply x y - multiplies two numbers\n/divide x y - divides two numbers (x / y)\n\nInline subcommands:\nshrug - sends an ascii shrug.")


help_handler = CommandHandler("help", helpme)
updater.dispatcher.add_handler(help_handler)


# ping command to make sure that the bot is alive
def pingpong(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Sensei")


ping_handler = CommandHandler("tamanegi", pingpong)
updater.dispatcher.add_handler(ping_handler)


# adds two numbers
def addcommand(bot, update, args):
    output = float(args[0]) + float(args[1])
    bot.sendMessage(chat_id=update.message.chat_id, text=output)


addition_handler = CommandHandler("add", addcommand, pass_args=True)
updater.dispatcher.add_handler(addition_handler)


# subtracts two numbers
def subtract(bot, update, args):
    output = float(args[0]) - float(args[1])
    bot.sendMessage(chat_id=update.message.chat_id, text=output)


subtraction_handler = CommandHandler("subtract", subtract, pass_args=True)
updater.dispatcher.add_handler(subtraction_handler)


# multiply two numbers
def multipl(bot, update, args):
    output = float(args[0]) * float(args[1])
    bot.sendMessage(chat_id=update.message.chat_id, text=output)


multiplication_handler = CommandHandler("multiply", multipl, pass_args=True)
updater.dispatcher.add_handler(multiplication_handler)


# divide two numbers
def divid(bot, update, args):
    output = float(args[0]) / float(args[1])
    bot.sendMessage(chat_id=update.message.chat_id, text=output)


division_handler = CommandHandler("divide", divid, pass_args=True)
updater.dispatcher.add_handler(division_handler)

# inline commands
def inlinestuff(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    print(query)
    if(query == "shrug"):
        results.append(InlineQueryResultArticle(id="shrug", title="¯\_(ツ)_/¯", input_message_content=InputTextMessageContent("¯\_(ツ)_/¯")))
    if(query == "ping"):
        results.append(InlineQueryResultArticle(id="ping", title="ping", input_message_content=InputTextMessageContent("pong")))
    update.inline_query.answer(results)
    #bot.answerInlineQuery("shrug", results)


inline_shrug_handler = InlineQueryHandler(inlinestuff)
updater.dispatcher.add_handler(inline_shrug_handler)

updater.dispatcher.add_error_handler(error)

updater.start_polling()