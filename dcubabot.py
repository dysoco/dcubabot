#!/usr/bin/python3
# -*- coding: utf-8 -*-
# STL imports

import sys

# Non STL imports
from telegram.ext import (Updater, CommandHandler)

# Local imports
from tokenz import *

"""
start: Mensaje al mandar start que es la priemra vez q un usuario habla con el bot, o si alguien pone /start
"""


def start(bot, update):
    update.message.reply_text("Hola, que tal? mandame /help si no sabes que puedo hacer!")


def help(bot, update):
    update.message.reply_text("Yo tampoco se que puedo hacer")


def estasvivo(bot, update):
    update.message.reply_text("Si, estoy vivo")


def main():
    try:
        global update_id
        # Telegram Bot Authorization Token
        botname = "DCUBABOT"
        print("Iniciando DCUBABOT")
        updater = Updater(token=token)
        dispatcher = updater.dispatcher
        j = updater.job_queue

        # Ven aca que tenemos un lindo codigo repetido.
        start_handler = CommandHandler('start', start)
        dispatcher.add_handler(start_handler)
        help_handler = CommandHandler('help', help)
        dispatcher.add_handler(help_handler)
        estasvivo_handler = CommandHandler('estasvivo', estasvivo)
        dispatcher.add_handler(estasvivo_handler)

        # Start running the bot
        updater.start_polling(clean=True)
    except Exception as inst:
        print("ERROR AL INICIAR EL DCUBABOT")
        result = str(type(inst)) + "\n"		# the exception instancee
        result += str(inst.args) + "\n"	 # arguments stored in .args
        # __str__ allows args to be printed directly,
        result += str(inst) + "\n"
        print(result)


if __name__ == '__main__':
    main()
