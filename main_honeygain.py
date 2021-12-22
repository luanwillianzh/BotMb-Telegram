import telebot
import os
import requests
from requests.structures import CaseInsensitiveDict
from telebot import types,util
from pathlib import Path
import json
import time

token = '2057686605:AAGSltSNs-s8231w7i4_9uJ9MXPaKi_IiyY'

bot = telebot.TeleBot(token, parse_mode="Markdown")

def extract_arg(arg):
    return arg.split()[1:]

@bot.message_handler(commands=['ping'])
def ping(message):
  bot.reply_to(message, "Pong!")

@bot.message_handler(commands=['honeygain'])
def honeygain(message):
  url = "https://dashboard.honeygain.com/api/v1/users/balances"

  headers = CaseInsensitiveDict()
  headers["authority"] = "dashboard.honeygain.com"
  headers["sec-ch-ua"] = '"Not A;Brand";v="99", "Chromium";v="96"'
  headers["accept"] = "application/json, text/plain, */*"
  headers["authorization"] = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE2NDAxMTY0NDgsImV4cCI6MTY3MTY1MjQ0OCwicm9sZXMiOlsiUk9MRV9VU0VSIiwiUk9MRV9UT1NfQUNDRVBURUQiLCJST0xFX0NPTkZJUk1FRF9FTUFJTCJdLCJlbWFpbCI6Imx1YW53aWxsaWFuemhAZ21haWwuY29tIn0.foejMXyHq7vlkq6poqjSHDjSJ_qqvaRCOrt5UcP1p7f4Gvjwq28GIrKvhTzLrNut3hOFW7nsYnKHW_0jgKDxg_v5eFzQaZ76EIFfIMRaCRdK-CrceGaneJTKp_cB8mG6JxOSCjR9SFMZrpWN99h0dNnr64xblX3AlSFU3CJyv0hFa-zMP_ZfH7x87MtfWYUOYItru4RNCIm1R1hU1lEqMElB9uSocGG4eioSDCWPujiFhHXGWbDGGG9dYHGCQt_DStXRKk0WNbvEMXZCVscfJ9bNvcL1NrSHEnY0Xhcrd1WW6wJ3uRsngnhlTpCU0Vu5LttzNzYlmxOQMqqlPXa6l4F27N-o9xqo-P8e19zPNrV4EI4eOnchpFb4jStGwVC0KXx4RgnPp3tYSnJ4gkCFieXteu724SwQgYemZJF0EHB-77EQgFvvD-z9ZSx8MKFq-6GavIattxqzFVyuWjEmbS0toAOdQWsKmbnqTb_s8Gvf_HArZjUuiezjl32F95wQ-wrz9XnN1rDA2IUvIJeHzDCNEg--T-bm3oqblS84NoUVJmSodCc8PmmMc8KWsOIrcM2ZJ0nProqYNP2A7D97zyhrFA6NupiTSSfsTT_EXAWeW63_e-1OkKs7cY2WkTIXxqNSDCCEmo0QQL1NPR9BuIQgy_2x8zBlU7mcd9wZT30"
  headers["sec-ch-ua-mobile"] = "?1"
  headers["user-agent"] = "Mozilla/5.0 (Linux; Android 6.0.1; SM-G532M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.46 Mobile Safari/537.36"
  headers["sec-ch-ua-platform"] = "Android"
  headers["sec-fetch-site"] = "same-origin"
  headers["sec-fetch-mode"] = "cors"
  headers["sec-fetch-dest"] = "empty"
  headers["referer"] = "https://dashboard.honeygain.com/"
  headers["accept-language"] = "pt-BR,pt;q=0.9,en-US;q=0.8,en;q=0.7"
  headers["cookie"] = "cookieConsent=%7B%22submitBasicData%22%3Atrue%2C%22submitUsageStats%22%3Atrue%2C%22submitAudienceData%22%3Atrue%7D; G_ENABLED_IDPS=google"
  data_honeygain = json.loads(requests.get(url, headers=headers).text)
  dolar = float((json.loads(requests.get("https://economia.awesomeapi.com.br/json/USD-BRL").text))[0]['high'])
  creditos = data_honeygain['data']['payout']['credits']
  try:
    cents = (data_honeygain['data']['payout']['usd_cents']) / 100
  except:
    cents = 0
  try: 
    usd = data_honeygain['data']['payout']['dolar']
  except:
    usd = 0
  ganho_usd = usd + cents
  ganho_brl = ganho_usd * dolar
  bot.reply_to(message, f"Créditos: {creditos}\r\nGanho (USD): {ganho_usd}\r\nGanho (BRL): {ganho_brl}")

@bot.message_handler(commands=['hora'])
def hora(message):
  t = time.localtime()
  current_time = time.strftime("%H:%M", t)
  msg = f'''A hora atual é: {current_time}'''
  bot.reply_to(message, msg)
def main():
    bot.infinity_polling(skip_pending=True)


if __name__ == '__main__':
    main()