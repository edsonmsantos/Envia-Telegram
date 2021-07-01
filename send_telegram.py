from telethon.sync import TelegramClient
from telethon.tl.types import InputPeerUser, InputPeerChannel
from telethon import TelegramClient, sync, events
import re
import time
import os
import json

api_id = ""
api_hash = ""
message = ""
timeout = 5

def sendTelegram(phone):
    client = TelegramClient('session', api_id, api_hash)
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Insira o código de autenticação enviado ao seu Telegram: '))
    try:
        receiver = phone
        client.send_message(receiver, message, parse_mode='html')
        print('Mensagem enviada para o número: ' + phone)
    except Exception as e:
        print(e)
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
        fileConfig = open('./config.json', 'r')
        config = json.load(fileConfig)
        global timeout
        global api_id
        global api_hash
        global message
        timeout = config["timeout"]
        api_id = config["api_id"]
        api_hash = config["api_hash"]
        message = config["message"]

loadConfig()
start('list.txt')
