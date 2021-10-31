import requests
from requests.structures import CaseInsensitiveDict

url = "https://www.tourovpn.com.br/ssh-gratis/conecta/transporta"

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/x-www-form-urlencoded"

data = "g-recaptcha-response=03AGdBq25xtwIrf6blz-I7nStUDLwe-P-Vo1yly-o282dd-1wc7prrW7HyTv_UjfxvhM5DT3NpKJssLn3JgR47epcfPbctOEZm7fKvK-mNsRHwdWaH40ZM1HmnciKlXY2lFmZnrUvWj6eN_SeTQpKXCS5ADL853LV_bRQho-oFE_DzVGAL8mGF_htpece4GSs5oRa6OptscimlQiV10ZezZDb6m4s4kGhlCvOs2UZ_MKY_6oI37CD6UwRLw58auvMF_dwaQ-0HAEmm_HBIMs0xhS3XHLhLiXwOdpmQXMjrEQeQhSfE8faAVbQ-UHiM3GJOJUo1lW9ikfM5ulHUDRt6xZ-HJzJjIgdkyrCHf0lYLleCGSL_JklH3CfjrO2oOyOSzj0g1QloQI29b1Ge3URDNdR7FDs4g18C9IdaHxpJxDyBiE7LgOXz0DF9GtLaW5q8N7nFwEyCS9EHQNEroFkvplDJo0UDF_xAlQ"


resp = requests.post(url, headers=headers, data=data)

str(resp.text).find("Usuário: touro")