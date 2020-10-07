import logging

import telegram
from telegram.ext import Updater, CommandHandler, InlineQueryHandler
from telegram.error import (TelegramError, Unauthorized, BadRequest, TimedOut,
                            ChatMigrated, NetworkError)

import functions.py

# Initialize bot #
bot = telegram.Bot(token="token")
updater = Updater(token="token")
debugging_on = False

# Handlers #
start_handler = CommandHandler("start", functions.start)
updater.dispatcher.add_handler(start_handler)

help_handler = CommandHandler("help", functions.help_me)
updater.dispatcher.add_handler(help_handler)

debug_handler = CommandHandler("amicute", functions.toggle_debug)
updater.dispatcher.add_handler(debug_handler)

ping_handler = CommandHandler("ointments", functions.pingpong)
updater.dispatcher.add_handler(ping_handler)

addition_handler = CommandHandler("add", functions.add_command, pass_args=True)
updater.dispatcher.add_handler(addition_handler)

subtraction_handler = CommandHandler("subtract", functions.subtract, pass_args=True)
updater.dispatcher.add_handler(subtraction_handler)

multiplication_handler = CommandHandler("multiply", functions.multipl, pass_args=True)
updater.dispatcher.add_handler(multiplication_handler)

division_handler = CommandHandler("divide", functions.divid, pass_args=True)
updater.dispatcher.add_handler(division_handler)

dice_handler = CommandHandler("roll", functions.diceroll, pass_args=True)
updater.dispatcher.add_handler(dice_handler)

inline_shrug_handler = InlineQueryHandler(functions.inline_stuff)
updater.dispatcher.add_handler(inline_shrug_handler)

getchathandler = CommandHandler("chatid", functions.getchatid)
updater.dispatcher.add_handler(getchathandler)

echo_handler = CommandHandler("echo", functions.echo)
updater.dispatcher.add_handler(echo_handler)

effective_handler = CommandHandler("effective.", functions.effective)
updater.dispatcher.add_handler(effective_handler)

badtime_handler = CommandHandler("badtime", functions.badtime)
updater.dispatcher.add_handler(badtime_handler)

updater.dispatcher.add_error_handler(functions.update_error)

updater.start_polling()
