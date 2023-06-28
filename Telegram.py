import requests
import time
import json
import os

class TelegramBot:
    def __init__(self):
        iTOKEN  = '6108844055:AAG7REAxPLmzPU_LAKDzFkagnlgGnU2npBc'
        self.iURL = f'https://api.telegram.org/bot{iTOKEN}/'

    def Iniciar(self):
        iUPDATE_ID = None
        while True:
            iATUALIZACAO = self.ler_novas_mensagens(iUPDATE_ID)
            IDADOS = iATUALIZACAO["result"]
            if IDADOS:
                for mensagem in IDADOS:
                    iUPDATE_ID = mensagem['update_id']
                    msg = mensagem["message"]["text"]
                    chat_id = mensagem["message"]["from"]["id"]
                    resposta = self.gerar_respostas(msg)
                    self.responder(resposta, chat_id)

    def ler_novas_mensagens(self, iUPDATE_ID):
        self.iLINK_REQ = f'{self.iURL}getUpdates?timeout=5'
        if iUPDATE_ID:
            self.iLINK_REQ = f'{self.iLINK_REQ}&offset={iUPDATE_ID + 1}'
        iRESULT = requests.get(self.iLINK_REQ)
        return json.loads(iRESULT.content)
    def gerar_respostas(self, msg):
        if msg == '/help':
            return 'bot feito para testes, me ignore'
        while msg not in '/start':
            return 'digite /start para começar'




    def responder(self, resposta, chat_id):
        self.iLINK_REQ = f'{self.iURL}sendMessage?chat_id={chat_id}&text={resposta}'
        requests.get(self.iLINK_REQ)



bot = TelegramBot()
bot.Iniciar()
