import telebot
from dotenv import load_dotenv
import os
import requests
from requests.structures import CaseInsensitiveDict
from telebot import types,util
from pathlib import Path
import json

load_dotenv()
token = '2057686605:AAGigkZfxLY_wEe3uC7v2S6GEaSlTvz4jTI'

bot = telebot.TeleBot(token, parse_mode="Markdown")

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['mb'])
def mb(message):
    status = extract_arg(message.text)
    if status == []:
      msg = '''Para receber mb envie seu accessPass com o comando /mb
      '''
      bot.reply_to(message, msg)
    else:
      headers = CaseInsensitiveDict()
      headers["Origin"] = "http://navegue.vivo.com.br"
      headers["Content-Type"] = "application/x-www-form-urlencoded"
      X9deToken2 = requests.post("http://e.vivo.ddivulga.com/api/v2.1/fetch", headers=headers, data=f'''slotId=%5B%7B%22slotId%22%3A102%2C%22target%22%3A%22slot%3D102%3Baamat%3Daamat3D19882337%3Badobeaamcookie%3DpossePre3D163978882Caamat3D19882337%3Bttu%3D0100007FD8F82C614D0723620299EE11%3Bgclau%3D1118538882921632093158%3BgaZX7D4NYJHK%3DGS11163209315710163209317146%3Bvivoprettycity%3DUyVDMyVBM28rUGF1bG8%3D%3Bfbp%3Dfb216321025485331651747283%3Baamuuid%3D27368184449230620631777943451298409598%3Bvivoregcity%3Dsaopaulo%3Bvivoregstate%3DSP%3Bregional%3DSP%3Bvivoregddd%3D11%3Bhjid%3Ded626780d5f94597b12dbf03c573f476%3Bcsc%3D1%3BCTRS%3DRecording%3BWRUIDCD%3D3474032550068585%3BAMCVF93F88C35ABCCD070A495CF840AdobeOrg%3D11241066807CMCIDTS7C188917CMCMID7C289750017116187312115408938543902396647CMCAAMLH16328724437C47CMCAAMB16328724437CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y7CMCOPTOUT1632274843s7CNONE7CMCCIDH7C13319136787CvVersion7C520%3Bcsid%3D7446c9b6736da532ae8de6f48f892f14163210852321632267696163226764515871178651666272523390%3BCTData%3Dgpv%3D3ckp%3Dcddm%3Dvivocombrapv15www44%3D4cpv15www44%3D3rpv15www44%3D3%3BgaGB9C14SX2D%3DGS11163227460731163227463532%3Bmbox%3DPCb79201a4e076420fae9791f9d7f0dfe03401696994391sessionf4b43fa1a5d44b1caff998388c8331e71633751668%3BgaDMLPJDP0E3%3DGS1116337495891116337498100%3Bga%3DGA1315675778471631021157%3Bgid%3DGA1310319720541633906861%3Bttnprf%3D%3BgatgtagUA1640616782%3D1%3BgatgtagUA1640616781%3D1%3Bttcvmt%3D1633992745%3Bttcc%3Ddirect%3Bttcs%3Ddirect%3Bttcm%3Ddirect%3Bttuus%3D1633992745047%3Bos%3Dandroid%3BtailCity%3Dcuiaba%3BtailtState%3Dmato%2520grosso%3BtailCountry%3Dbr%3BtailEquipment%3D9%3BtailGender%3Dbr%22%7D%5D&pageId=660224&insertionId=&insertionUUID=&insertionType=&referer=http%3A%2F%2Finternetgratis.vivo.com.br%2F&accessPass={status[0]}''')
      X9deToken2 = json.loads(X9deToken2.text)
      try:
        bot.reply_to(message, f'''Seu número é: {X9deToken2['msisdn']}''')
      except:
        bot.reply_to(message, f'''Token Inválido''')
      os.system(f'''python3 mb.py {status[0]}''')

@bot.message_handler(commands=['payload'])
def payload(message):
    status = extract_arg(message.text)
    if status == []:
      msg = '''Para gerar uma payload com host personalizado, envie o host usando o comando /payload!

Ex: /payload teste.tourovpn.com.br
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
    msg = '''Olá, sou o bot de SSH do grupo [Nᴇᴛ ɢʀᴀ́ᴛɪs ᴄʜᴀᴛ](https://t.me/internetgratisvivoemais)
Envie /ssh para receber uma conta ssh.
Envie /ws para receber uma lista de proxy websocket.
Envie /payload para gerar payload customizada.'''
    bot.reply_to(message, msg)

@bot.message_handler(commands=['ping'])
def ping(message):
  bot.reply_to(message, "Pong!")


@bot.message_handler(commands=['ssh'])
def ssh(message):
    bot.send_message(1374108361, )
    if message.chat.type == "private":
      os.system("bash create_ssh.sh")
      ssh_user = Path('ssh_user.txt').read_text().replace(' Usuário: ', '').replace('\n', '')
      ssh_pass = Path('ssh_pass.txt').read_text().replace('Senha: ', '').replace('\n', '')
      msg = f'''=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                   CONTA SSH
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Usuário: `{ssh_user}`
Senha: `{ssh_pass}`
Host: `teste.tourovpn.com.br`


=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
                    PAYLOADS
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

Websocket: `GET /? HTTP/1.0[lf]Host: teste.tourovpn.com.br[lf]Upgrade: websocket[lf]Connection: Keep-Alive[lf]User-Agent: [ua][lf]Referer: [lf][lf]`

Websocket Proxy: `GET / HTTP/1.1[crlf]Host: teste.tourovpn.com.br[crlf]Upgrade: websocket[crlf][crlf]`'''
      bot.reply_to(message, msg)
    else:
      bot.reply_to(message, "Comando não liberado para grupos, vem no pv!")


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