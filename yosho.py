import telegram
import random
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from telegram.error import TelegramError, Unauthorized, BadRequest, TimedOut, ChatMigrated, NetworkError
import logging

# initialize bot and logging for debugging #
bot = telegram.Bot(token="token")
updater = Updater(token="token")
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
                    text="Available commands:\n/echo text - echoes text\n/roll x - rolls a number between 1 and x\n/add x y - adds two numbers\n/subtract x y - subtracts two numbers (x - y)\n/multiply x y - multiplies two numbers\n/divide x y - divides two numbers (x / y)\n\nInline subcommands:\nshrug - sends an ascii shrug.\nbadtime - fucken love undertale")


help_handler = CommandHandler("help", helpme)
updater.dispatcher.add_handler(help_handler)

debuggingon = False

def toggledebug(bot, update):
    global debuggingon
    if debuggingon:
        bot.sendMessage(chat_id=update.message.chat_id, text="No")
        debuggingon = False
        return
    if not debuggingon:
        bot.sendMessage(chat_id=update.message.chat_id, text="Yes")
        debuggingon = True
        return

debug_handler = CommandHandler("amicute", toggledebug)
updater.dispatcher.add_handler(debug_handler)

# ping command to make sure that the bot is alive
def pingpong(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Ointments.")


ping_handler = CommandHandler("ointments", pingpong)
updater.dispatcher.add_handler(ping_handler)


# adds numbers
def addcommand(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text="Incorrect usage.\n\nUsage: `/add x y z ...`", parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        output = 0
        tick = -1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debuggingon:
                bot.sendMessage(chat_id=update.message.chat_id, text="value of args[" + tick + "]: " + i)
            i = int(i)
            output = output + i
        output = str(output)
        if debuggingon:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)


addition_handler = CommandHandler("add", addcommand, pass_args=True)
updater.dispatcher.add_handler(addition_handler)


# subtracts numbers
def subtract(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text="Incorrect usage.\n\nUsage: `/subtract x y z ...`\n(it subtracts left to right be careful of order)", parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        output = int(args[0])
        tick = -1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debuggingon:
                bot.sendMessage(chat_id=update.message.chat_id, text="value of args[" + tick + "]: " + i)
            i = int(i)
            if tick != "0": #don't subtract the very first tick, cause then you'd subtract args[0] from args[0], bad
                output = output - i
        output = str(output)
        if debuggingon:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)


subtraction_handler = CommandHandler("subtract", subtract, pass_args=True)
updater.dispatcher.add_handler(subtraction_handler)


# multiply two numbers
def multipl(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text="Incorrect usage.\n\nUsage: `/multiply x y z ...`", parse_mode=telegram.ParseMode.MARKDOWN)

    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        tick = -1
        output = 1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debuggingon:
                bot.sendMessage(chat_id=update.message.chat_id, text="value of args[" + tick + "]: " + i)
            i = int(i)
            output = output * i
        output = str(output)
        if debuggingon:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)


multiplication_handler = CommandHandler("multiply", multipl, pass_args=True)
updater.dispatcher.add_handler(multiplication_handler)


# divide two numbers
def divid(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text="Incorrect usage.\n\nUsage: `/divide x y z ...`\n(it divides left to right be careful of order)", parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        output = int(args[0])
        tick = -1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debuggingon:
                bot.sendMessage(chat_id=update.message.chat_id, text="value of args[" + tick + "]: " + i)
            i = int(i)
            if tick != "0": #don't subtract the very first tick, cause then you'd subtract args[0] from args[0], bad
                output = output / i
        output = str(output)
        if debuggingon:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)


division_handler = CommandHandler("divide", divid, pass_args=True)
updater.dispatcher.add_handler(division_handler)

def diceroll(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text="Incorrect usage.\n\nUsage: `/roll <range>`", parse_mode=telegram.ParseMode.MARKDOWN)
        return
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        num = int(args[0])
        output = str(random.randint(1,num))
        bot.sendMessage(chat_id=update.message.chat_id, text=output)

dice_handler = CommandHandler("roll", diceroll, pass_args=True)
updater.dispatcher.add_handler(dice_handler)

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
    if (query == "badtime"):
        results.append(InlineQueryResultArticle(id="badtime", title="fucken love undertale", input_message_content=InputTextMessageContent("…………/´¯/)…………….(\¯`.…………..\n………../…//……….i…….\….…………..\n………./…//…fuken luv….\….………….\n…../´¯/…./´¯..undertale./¯` .…\¯`.…….\n.././…/…./…./.|_.have._|..….……..…..\n(.(b.(..a.(..d./..)..)……(..(." + "\\" + "ti.)..m.)..e.).)….\n..……………\/…/………\/……………./….\n……………….. /……….……………..")))
    update.inline_query.answer(results)
    #bot.answerInlineQuery("shrug", results)


inline_shrug_handler = InlineQueryHandler(inlinestuff)
updater.dispatcher.add_handler(inline_shrug_handler)


def getchatid(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.chat_id)

getchathandler = CommandHandler("chatid", getchatid)
updater.dispatcher.add_handler(getchathandler)

def echo(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    reply = update.message.text[6:]
    if reply == "":
        bot.sendMessage(chat_id=update.message.chat_id, text="Gimmie some text to echo!")
        return
    if reply == "Gimmie some text to echo!":
        bot.sendMessage(chat_id=update.message.chat_id, text="That's my line.")
        return
    if reply != "":
        bot.sendMessage(chat_id=update.message.chat_id, text=reply)
        return

echo_handler = CommandHandler("echo", echo)
updater.dispatcher.add_handler(echo_handler)

def effective(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Power لُلُصّ؜بُلُلصّبُررًً ॣ h؜ ॣ؜ ॣ ॣ')

effective_handler = CommandHandler("effective.", effective)
updater.dispatcher.add_handler(effective_handler)

def badtime(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="…………/´¯/)…………….(\¯`.…………..\n………../…//……….i…….\….…………..\n………./…//…fuken luv….\….………….\n…../´¯/…./´¯..undertale./¯` .…\¯`.…….\n.././…/…./…./.|_.have._|..….……..…..\n(.(b.(..a.(..d./..)..)……(..(." + "\\" + "ti.)..m.)..e.).)….\n..……………\/…/………\/……………./….\n……………….. /……….……………..")

badtime_handler = CommandHandler("badtime", badtime)
updater.dispatcher.add_handler(badtime_handler)

updater.dispatcher.add_error_handler(error)

updater.start_polling()
