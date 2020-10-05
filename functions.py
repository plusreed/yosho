#Functions for yosho.py
from random import randint
import logging

import telegram
from telegram import InlineQueryResultArticle, InputTextMessageContent

# Initialize logging for debugging #
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def update_error(bot, update, error):
    """Logs errors related to updates"""
    logger.warning('Update "%s" caused error "%s"' % (update, error))

# start text #
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, 
                    text="Hi. I do a bunch of misc shit. Add me to a group I guess")

# help command #
def help_me(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text=("Available commands: \
                        \n/echo text - echoes text \
                        \n/roll x - rolls a number between 1 and x \
                        \n/add x y - adds two numbers \
                        \n/subtract x y - subtracts two numbers (x - y) \
                        \n/multiply x y - multiplies two numbers \
                        \n/divide x y - divides two numbers (x / y) \
                        \n\nInline subcommands: \
                        \nshrug - sends an ascii shrug. \
                        \nbadtime - fucken love undertale")
                    )

def toggle_debug(bot, update):
    global debugging_on
    if debugging_on:
        bot.sendMessage(chat_id=update.message.chat_id, text="No")
        debugging_on = False
        return
    if not debugging_on:
        bot.sendMessage(chat_id=update.message.chat_id, text="Yes")
        debugging_on = True
        return

# ping command to make sure that the bot is alive #
def pingpong(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Ointments.")

# Math commands #
# adds numbers
def add_command(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text=("Incorrect usage. \
                        \n\nUsage: `/add x y z ...`"),
                        parse_mode=telegram.ParseMode.MARKDOWN
                        )
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        output = 0
        tick = -1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debugging_on:
                bot.sendMessage(chat_id=update.message.chat_id, 
                                text="value of args[" + tick + "]: " + i)
            i = int(i)
            output = output + i
        output = str(output)
        if debugging_on:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)

# subtracts numbers #
def subtract(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text=("Incorrect usage. \
            \n\nUsage: `/subtract x y z ...` \
            \n(it subtracts left to right be careful of order)"),
            parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        output = int(args[0])
        tick = -1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debugging_on:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text=("value of args[" + tick + "]: " + i))
            i = int(i)
            if tick != "0":
                #don't subtract the very first tick, cause then you'd subtract
                # args[0] from args[0],bad
                output = output - i
        output = str(output)
        if debugging_on:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)

# multiply two numbers #
def multipl(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text=("Incorrect usage. \
            \n\nUsage: `/multiply x y z ...`"),
            parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        tick = -1
        output = 1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debugging_on:
                bot.sendMessage(chat_id=update.message.chat_id,
                                text=("value of args[" + tick + "]: " + i))
            i = int(i)
            output = output * i
        output = str(output)
        if debugging_on:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)

# divide two numbers
def divid(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id, text=("Incorrect usage. \
            \n\nUsage: `/divide x y z ...` \
            \n(it divides left to right be careful of order)"),
            parse_mode=telegram.ParseMode.MARKDOWN)
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        output = int(args[0])
        tick = -1
        for i in args:
            tick = int(tick)
            tick = tick + 1
            tick = str(tick)
            if debugging_on:
                bot.sendMessage(chat_id=update.message.chat_id,
                                 text=("value of args[" + tick + "]: " + i))
            i = int(i)
            if tick != "0":
                #don't subtract the very first tick, cause then you'd 
                # subtract args[0] from args[0], bad
                output = output / i
        output = str(output)
        if debugging_on:
            bot.sendMessage(chat_id=update.message.chat_id, text="result: " + output)
        else:
            bot.sendMessage(chat_id=update.message.chat_id, text=output)

def diceroll(bot, update, args):
    if(args == []):
        bot.sendMessage(chat_id=update.message.chat_id,
                        text=("Incorrect usage.\n\nUsage: `/roll <range>`"),
                        parse_mode=telegram.ParseMode.MARKDOWN
                        )
    else:
        bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
        num = int(args[0])
        output = str(randint(1,num))
        bot.sendMessage(chat_id=update.message.chat_id, text=output)
    return

# inline commands #
def inline_stuff(bot, update):
    query = update.inline_query.query
    if not query:
        return
    results = list()
    print(query)
    if(query == "shrug"):
        results.append(InlineQueryResultArticle(id="shrug",
                                                title="¯\_(ツ)_/¯",
                                                input_message_content=InputTextMessageContent(
                                                    "¯\_(ツ)_/¯")))
    if(query == "ping"):
        results.append(InlineQueryResultArticle(id="ping",
                                                title="ping",
                                                input_message_content=InputTextMessageContent(
                                                    "pong")))
    if (query == "badtime"):
        results.append(InlineQueryResultArticle(id="badtime",
                                                title="fucken love undertale",
                                                input_message_content=InputTextMessageContent(
                                                    "…………/´¯/)…………….(\¯`.…………..\
                                                        \n………../…//……….i…….\….…………..\
                                                        \n………./…//…fuken luv….\….………….\
                                                        \n…../´¯/…./´¯..undertale./¯` .…\¯`.…….\
                                                        \n.././…/…./…./.|_.have._|..….……..…..\
                                                        \n(.(b.(..a.(..d./..)..)……(..(." 
                                                        + "\\" + "ti.)..m.)..e.).)….\
                                                            \n..……………\/…/………\/……………./….\
                                                            \n……………….. /……….……………..")))
    update.inline_query.answer(results)
    #bot.answerInlineQuery("shrug", results)

def getchatid(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text=update.message.chat_id)

def echo(bot, update):
    bot.sendChatAction(chat_id=update.message.chat_id, action=telegram.ChatAction.TYPING)
    reply = update.message.text[6:]
    if reply == "":
        bot.sendMessage(chat_id=update.message.chat_id, text="Gimmie some text to echo!")
    elif reply == "Gimmie some text to echo!":
        bot.sendMessage(chat_id=update.message.chat_id, text="That's my line.")
    else:
        bot.sendMessage(chat_id=update.message.chat_id, text=reply)
    return

def effective(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='Power لُلُصّ؜بُلُلصّبُررًً ॣ h؜ ॣ؜ ॣ ॣ')

def badtime(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id,
                    text="…………/´¯/)…………….(\¯`.…………..\
                        \n………../…//……….i…….\….…………..\
                        \n………./…//…fuken luv….\….………….\
                        \n…../´¯/…./´¯..undertale./¯` .…\¯`.…….\
                        \n.././…/…./…./.|_.have._|..….……..…..\
                        \n(.(b.(..a.(..d./..)..)……(..(."
                        + "\\" + "ti.)..m.)..e.).)….\
                            \n..……………\/…/………\/……………./….\
                            \n……………….. /……….…………….."
                    )
