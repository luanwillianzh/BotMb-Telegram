#!/usr/bin/python
import os
import time
import requests
import json
import sys
from requests.structures import CaseInsensitiveDict
def Main():
 option = int(sys.argv[1])
 sctoken = str(sys.argv[2])


 if option == 1:
  nop = 10
  UrlReward="http://e.vivo.ddivulga.com/api/clickEvent"
  data = f"slotId=%5B%7B%22slotId%22%3A%22101%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22102%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22103%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22104%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22105%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22106%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22107%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22108%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22109%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=660224&insertionId=&insertionUUID=&insertionType=&referer=http%3A%2F%2Finternetgratis.vivo.com.br%2F&accessPass={sctoken}"
  url = "http://e.vivo.ddivulga.com/api/v2.1/fetch"
  headers = CaseInsensitiveDict()
  headers["Origin"] = "http://a.vivo.ddivulga.com"
  headers["Content-Type"] = "application/x-www-form-urlencoded"
  reapit=100
   
  
  
 elif option == 2:
  nop = 30
  UrlReward="http://e.oi.ddivulga.com/api/clickEvent"
  data = f"slotId=%5B%7B%22slotId%22%3A301%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Dmanaus%3BtailtState%3Damazonas%3BtailCountry%3Dbr%22%7D%5D&pageId=822068&insertionId=&insertionUUID=&insertionType=ANY&referer=&accessPass={sctoken}"
  url = "http://e.oi.ddivulga.com/api/v2.1/fetch"
  headers = CaseInsensitiveDict()
  headers["Origin"] = "http://e.oi.ddivulga.com"
  headers["Referer"] = "http://e.oi.ddivulga.com"
  headers["Content-Type"] = "application/x-www-form-urlencoded"
  reapit=100

 advid = [ ]
 impressionid = [ ]
 tokens_on = 0
 iu = 0
 AdvName = [ ]
 adsON = "Mercedes"
 try:
  X9deToken = json.loads(requests.post(url, headers=headers, data=data).text)

 except:
  exit()

 tokensnovos = 0
 while iu < 9:
  iu = iu + 1
  teste = f"{nop}{iu}"
  print(teste)
  try:
   advidchecar = (X9deToken[f'{teste}']['advId'])
   
   if advidchecar in advid:
    pass
   else:
    advid.append(X9deToken[f'{teste}']['advId'])
   
   impressionidcheck = (X9deToken[f'{teste}']['impressionEventId'])
   
   if impressionidcheck in impressionid:
    pass
   else:
    impressionid.append(X9deToken[f'{teste}']['impressionEventId'])
   
   AdvNamecheck = (X9deToken[f'{teste}']['advName'])
   
   if AdvNamecheck in AdvName:
    pass
   
   else:   
    AdvName.append(X9deToken[f'{nop}{iu}']['advName'])
   
   tokens_on = tokens_on + 1
   tokensnovos = tokensnovos + 1
   adsON = "Audi"
  except:
   pass
   
 headersi = CaseInsensitiveDict()
 headersi["Content-Type"] = "application/x-www-form-urlencoded"

 testador = 0
 testestokens = 0
 for token in range(tokens_on):
  
  testador = testador + 1
  try:
    contagem = 0
    while contagem < reapit:
      
      time.sleep(0.7)
      contagem = contagem + 1
      
      resp = requests.post(UrlReward, headers=headers, data=f"advId={advid[token]}&eventImpressionId={impressionid[token]}&apass={sctoken}").text
      print(resp)
      if 'evtClickId' in resp:
        print()
      else:
        contagem = reapit
  except:
    pass
    
 testestokens = testestokens + 1
 
Main()
