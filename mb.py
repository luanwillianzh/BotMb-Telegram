import requests
from requests.structures import CaseInsensitiveDict
import json
import sys

#accessPass = str(sys.argv[1])
accessPass = "h8d_IZY7QEblZzxOEAvgXwWkDgjlhK2DeeiRP2QDyjw5qLBzGWkEnMUi77zlJ2q"

headers = CaseInsensitiveDict()
headers["Origin"] = "http://a.vivo.ddivulga.com"
headers["Content-Type"] = "application/x-www-form-urlencoded"

X9deToken = requests.post("http://e.vivo.ddivulga.com/api/v2.1/fetch", headers=headers, data=f'''slotId=%5B%7B%22slotId%22%3A%22101%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Drio%2520de%2520janeiro%3BtailtState%3Drio%2520de%2520janeiro%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22102%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Drio%2520de%2520janeiro%3BtailtState%3Drio%2520de%2520janeiro%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22103%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Drio%2520de%2520janeiro%3BtailtState%3Drio%2520de%2520janeiro%3BtailCountry%3Dbr%22%7D%2C%7B%22slotId%22%3A%22104%22%2C%22target%22%3A%22os%3Dandroid%3BtailCity%3Drio%2520de%2520janeiro%3BtailtState%3Drio%2520de%2520janeiro%3BtailCountry%3Dbr%22%7D%5D&pageId=660224&insertionId=&insertionUUID=&insertionType=&referer=http%3A%2F%2Finternetgratis.vivo.com.br%2F&accessPass={accessPass}''')

X9deToken = json.loads(X9deToken.text)
print(X9deToken)
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

print(f"Token(s) On: {tokens_on}")
headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

for token in range(5):
  try:
    for i in range(10):
      requests.post("http://e.vivo.ddivulga.com/api/clickEvent", headers=headers, data=f"advId={advid[token - 1]}&eventImpressionId={impressionid[token - 1]}&apass={accessPass}")
  except:
    pass