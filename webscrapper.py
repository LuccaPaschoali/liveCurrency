from gettext import gettext
import requests
from bs4 import BeautifulSoup
import tkinter

#Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36

#dolar
headers_dolar = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
page_dolar = requests.get("https://www.google.com/search?q=dolar+real&rlz=1C1AVUC_enBR807BR827&oq=dolar+real&aqs=chrome..69i57j0i131i433i512j0i512l8.3529j1j15&sourceid=chrome&ie=UTF-8", headers = headers_dolar)
soup_dolar = BeautifulSoup(page_dolar.content, 'html.parser')
valor_dolar = soup_dolar.find("span", class_= "DFlfde SwHCTb")


#rublo russo
headers_rublo = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
page_rublo = requests.get("https://www.google.com/search?q=rublo+real&rlz=1C1AVUC_enBR807BR827&biw=1366&bih=657&sxsrf=APq-WBt3ha9nM0qfmjMjyYSkZI-SStli3w%3A1646167038737&ei=_oMeYpXYLNXB5OUPx8WMmAc&ved=0ahUKEwiVz9aM4qX2AhXVILkGHcciA3MQ4dUDCA4&uact=5&oq=rublo+real&gs_lcp=Cgdnd3Mtd2l6EAMyCQgjECcQRhCCAjIFCAAQgAQyBAgAEEMyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQFhAKEB4yBggAEBYQHjIGCAAQFhAeOgQIIxAnOgYIIxAnEBM6CggAELEDEIMBEEM6CgguELEDEIMBEEM6CAgAELEDEIMBOgsIABCABBCxAxCDAToECAAQAzoECAAQCkoECEEYAEoECEYYAFAAWL0MYJwPaABwAXgAgAGHAYgB_AiSAQQwLjEwmAEAoAEBwAEB&sclient=gws-wiz", headers = headers_rublo)
soup_rublo = BeautifulSoup(page_rublo.content, 'html.parser')
valor_rublo = soup_rublo.find("span", class_= "DFlfde SwHCTb")


#euro
headers_euro = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
page_euro = requests.get("https://www.google.com/search?q=euro+real&rlz=1C1AVUC_enBR807BR827&biw=1366&bih=657&sxsrf=APq-WBvZq9G2519KeM1uos9JVJ9sa-EQTQ%3A1646167045618&ei=BYQeYqCmJfO85OUPjqyUyAQ&ved=0ahUKEwjgvPqP4qX2AhVzHrkGHQ4WBUkQ4dUDCA4&uact=5&oq=euro+real&gs_lcp=Cgdnd3Mtd2l6EAMyDwgAELEDEIMBEEMQRhCCAjILCAAQgAQQsQMQgwEyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDIFCAAQgAQyBQgAEIAEMgUIABCABDoKCAAQsQMQgwEQQzoHCAAQsQMQQzoECAAQQzoQCAAQgAQQsQMQgwEQRhCCAjoICAAQsQMQgwE6CwguEIAEEMcBEK8BSgQIQRgASgQIRhgAUABY9gpgoA1oAHABeAGAAYwCiAHPCZIBBTAuOC4xmAEAoAEBwAEB&sclient=gws-wiz", headers = headers_euro)
soup_euro = BeautifulSoup(page_euro.content, 'html.parser')
valor_euro = soup_euro.find("span", class_= "DFlfde SwHCTb")


#renminbi
headers_renminbi = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
page_renminbi = requests.get("https://www.google.com/search?q=Remimbi&rlz=1C1AVUC_enBR807BR827&sxsrf=APq-WBsIrB2rjlyjSjANqhN7Kkc-0RvM2A%3A1646168116462&ei=NIgeYrbjG_-45OUP7bKL2AU&ved=0ahUKEwi2zcmO5qX2AhV_HLkGHW3ZAlsQ4dUDCA4&uact=5&oq=Remimbi&gs_lcp=Cgdnd3Mtd2l6EAMyCggAELEDEIMBEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAoyBAgAEAo6BwgAEEcQsANKBAhBGABKBAhGGABQpARYpARgnwVoAXABeACAAW2IAW2SAQMwLjGYAQCgAQHIAQfAAQE&sclient=gws-wiz", headers = headers_renminbi)
soup_renminbi = BeautifulSoup(page_renminbi.content, 'html.parser')
valor_renminbi = soup_renminbi.find("span", class_= "DFlfde SwHCTb")


#iene
headers_iene = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36'}
page_iene = requests.get("https://www.google.com/search?q=iene&rlz=1C1AVUC_enBR807BR827&oq=iene&aqs=chrome..69i57j0i433i512j0i131i433i512l2j0i512j0i433i512l2j0i512l2j46i175i199i512.596j0j9&sourceid=chrome&ie=UTF-8", headers = headers_iene)
soup_iene = BeautifulSoup(page_iene.content, 'html.parser')
valor_iene = soup_iene.find("span", class_= "DFlfde SwHCTb")

print("Moedas disponíveis: Dolar, Euro, Rublo, Renminbi, Iene e Real")
print("Dolar: R$", valor_dolar.text)
print("Rublo: R$", valor_rublo.text)
print("Euro: R$", valor_euro.text)
print("Renminbi: R$", valor_renminbi.text)
print("Iene: R$", valor_iene.text)