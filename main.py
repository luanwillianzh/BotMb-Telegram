import telebot
import os
import requests
from requests.structures import CaseInsensitiveDict
from telebot import types, util
from pathlib import Path
import json

token = '2057686605:AAGigkZfxLY_wEe3uC7v2S6GEaSlTvz4jTI'

bot = telebot.TeleBot(token, parse_mode="Markdown")

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['vivo'])
def vivo(message):
    status = extract_arg(message.text)
    if status == []:
      msg = '''Para receber mb envie seu accessPass com o comando /vivo
      '''
      bot.reply_to(message, msg)
    else:
      headers = CaseInsensitiveDict()
      headers["Origin"] = "http://navegue.vivo.com.br"
      headers["Content-Type"] = "application/x-www-form-urlencoded"
      X9deToken2 = requests.post("http://e.vivo.ddivulga.com/api/v2.1/fetch", headers=headers, data=f'''slotId=%5B%7B%22slotId%22%3A%22101%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22102%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22103%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22104%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22105%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22106%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22107%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22108%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22109%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=660224&insertionId=&insertionUUID=&insertionType=&referer=http%3A%2F%2Finternetgratis.vivo.com.br%2F&accessPass={status[0]}''')
      X9deToken = json.loads(X9deToken2.text)
      print(status[0])
      print(X9deToken)
      try:
        tokens_on = 0
        advid = []
        impressionid = []
        try:
          advid.append(X9deToken['101']['advId'])
          impressionid.append(X9deToken['101']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['102']['advId'])
          impressionid.append(X9deToken['102']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['103']['advId'])
          impressionid.append(X9deToken['103']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['104']['advId'])
          impressionid.append(X9deToken['104']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['105']['advId'])
          impressionid.append(X9deToken['105']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          bot.reply_to(message, f'''Olá [{message.from_user.first_name}](tg://user?id={message.from_user.id})\r\nTokens on: {tokens_on}''')
        except:
          pass
      except:
        bot.reply_to(message, f'''Token Inválido''')
      os.system(f'''screen python3 force.py 1 {status[0]}''')
      bot.delete_message(message.chat.id, message.id, timeout=None)

@bot.message_handler(commands=['oi'])
def oi(message):
    status = extract_arg(message.text)
    if status == []:
      msg = '''Para receber mb envie seu accessPass com o comando /oi
      '''
      bot.reply_to(message, msg)
    else:
      headers = CaseInsensitiveDict()
      headers["Origin"] = "http://e.oi.ddivulga.com"
      headers["Content-Type"] = "application/x-www-form-urlencoded"
      X9deToken2 = requests.post("http://e.oi.ddivulga.com/api/v2.1/fetch", headers=headers, data=f'''slotId=%5B%7B%22slotId%22%3A301%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=822068&insertionId=&insertionUUID=&insertionType=ANY&referer=&accessPass={status[0]}''')
      X9deToken = json.loads(X9deToken2.text)
      print(X9deToken)
      print(status[0])
      try:
        tokens_on = 0
        advid = []
        impressionid = []
        try:
          advid.append(X9deToken['301']['advId'])
          impressionid.append(X9deToken['301']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['302']['advId'])
          impressionid.append(X9deToken['302']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['303']['advId'])
          impressionid.append(X9deToken['303']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['304']['advId'])
          impressionid.append(X9deToken['304']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          advid.append(X9deToken['305']['advId'])
          impressionid.append(X9deToken['305']['impressionEventId'])
          tokens_on = tokens_on + 1
        except:
          pass
        try:
          bot.reply_to(message, f'''Olá [{message.from_user.first_name}](tg://user?id={message.from_user.id})\r\nTokens on: {tokens_on}''')
        except:
          pass
      except:
        bot.reply_to(message, f'''Token Inválido''')
      os.system(f'''screen python3 force.py 2 {status[0]}''')
      bot.delete_message(message.chat.id, message.id, timeout=None)

@bot.message_handler(commands=['payload'])
def payload(message):
    status = extract_arg(message.text)
    if status == []:
      msg = '''Para gerar uma payload com host personalizado, envie o host usando o comando /payload!

Ex: /payload teste.example.xyz
      '''
      bot.reply_to(message, msg)
    else:
      msg = f'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                    PAYLOADS
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Websocket: `GET /? HTTP/1.0[lf]Host: {status[0]}[lf]Upgrade: websocket[lf]Connection: Keep-Alive[lf]User-Agent: [ua][lf]Referer: [lf][lf]`

Websocket Proxy: `GET / HTTP/1.1[crlf]Host: {status[0]}[crlf]Upgrade: websocket[crlf][crlf]`'''
      bot.reply_to(message, msg)

    
@bot.message_handler(commands=['start'])
def greet(message):
    msg = f'''Olá {message.from_user.first_name}, sou um bot feito pelo @luanw04
Envie /oi para receber mbs na oi.
Envie /vivo para receber mbs na vivo.
Envie /ws para receber uma lista de proxy websocket.
Envie /payload para gerar payload customizada.
Envie /cpf para fazer uma consulta cpf.
Envie /nome para consultar nome.'''
    bot.reply_to(message, msg)

@bot.message_handler(commands=['ping'])
def ping(message):
  bot.reply_to(message, "Pong!")

@bot.message_handler(commands=['cpf'])
def cpf(message):
  status = extract_arg(message.text)
  if status == []:
    msg = '''Envie o cpf usando o comando /cpf:
Ex: /cpf 12345678900'''
    bot.reply_to(message, msg)
  else:
    resp = requests.get(f"http://ghostcenter.xyz/api/cpf/{status[0]}")
    resp = json.loads(resp.text)
    if resp['status'] == 200:
      bot.reply_to(message, f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\r\n      DADOS ENCONTRADOS\r\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\r\n\r\nCPF: {resp['dados']['cpf']}\r\nNOME: {resp['dados']['nome']}\r\nDATA DE NASCIMENTO: {resp['dados']['nascimento']}\r\nSEXO: {resp['dados']['sexo']}")
    else:
      bot.reply_to(message, "Cpf Inválido!")

@bot.message_handler(commands=['nome'])
def nome(message):
  status = extract_arg(message.text)
  if status == []:
    msg = '''Envie o nome usando o comando /nome:
Ex: /nome Fulano da Silva'''
    bot.reply_to(message, msg)
  else:
    nome = str(status).replace('[', '').replace("'", "").replace(", ", " ").replace("]", "")
    resp = requests.get(f"http://ghostcenter.xyz/api/nome/{nome}")
    resp = json.loads(resp.text)
    if resp['status'] == 200:
      for i in resp['dados']:
        bot.reply_to(message, f"=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\r\n      DADOS ENCONTRADOS\r\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=\r\n\r\nCPF: {i['cpf']}\r\nNOME: {i['nome']}\r\nDATA DE NASCIMENTO: {i['nascimento']}\r\nSEXO: {i['sexo']}")
    else:
      bot.reply_to(message, "Nome Inválido!")

@bot.message_handler(commands=['ws'])
def ws(message):
    msg = f'''Lista de Proxy WS

`104.16.85.20` (Claro)
`104.16.86.20` (Claro)
`104.16.87.20` (Claro)
`104.16.88.20` (Claro)
`104.16.89.20` (Claro)
`104.18.7.80` (Vivo)
`104.16.56.6` (Vivo)
`104.16.57.6` (Vivo)
`104.18.6.80` (Vivo)
`104.18.7.80` (Vivo)
`104.16.18.94` (Vivo Tim)
`104.16.19.94` (Vivo Tim)'''
    bot.reply_to(message, msg)

def main():
    bot.infinity_polling(skip_pending=True)


if __name__ == '__main__':
    main()
