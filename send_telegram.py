# -*- coding: utf-8 -*-
from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import re
import time
import os
import json
import codecs

api_id = ""
api_hash = ""
message = ""
timeout = 5
senderPhone = ""

def sendTelegram(phone):
    client = TelegramClient('session', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(senderPhone)
        client.sign_in(senderPhone, input('Insira o código de login do Telegram: '))
    try:
        receiver = phone
        client.send_message(receiver, message, parse_mode='html')
        saveLog('success.txt', phone)
        print('Mensagem enviada para o número: ' + phone)
    except Exception as e:
        print(e)
        saveLog('error.txt', phone)
    client.disconnect()

def start(filename):
    if (not os.path.exists(filename)):
        print('Arquivo de lista não encontrado')
    else:
        fileList = open(filename, 'r')
        for line in fileList:
            try:
                number = re.sub('[^0-9]', '', line)
                print('Enviando para ' + number)
                sendTelegram(number)
                time.sleep(timeout)
            except Exception as e:
                print(e)

def loadConfig():
    if (not os.path.exists('./config.json')):
        print('Arquivo de configuração não encontrado')
    else:
        fileConfig = codecs.open('./config.json', 'r', encoding='utf-8')
        config = json.load(fileConfig)
        global timeout
        global api_id
        global api_hash
        global message
        global senderPhone
        timeout = config["timeout"]
        api_id = config["api_id"]
        api_hash = config["api_hash"]
        message = config["message"]
        senderPhone = config["myPhone"]
        fileConfig.close()

def saveLog(filename, content):
    f = open(filename, "a")
    f.write(content + "\r")
    f.close()

loadConfig()
start('list.txt')
