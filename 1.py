
import requests
from BeautifulSoup import BeautifulSoup

doc  = requests.get('https://www.sas.am/categories/%D5%80%D5%A1%D6%81%D5%A1%D5%A2%D5%B8%D6%82%D5%AC%D5%AF%D5%A5%D5%B2%D5%A5%D5%B6_%D6%87_%D5%A9%D5%AD%D5%BE%D5%A1%D5%AE%D6%84%D5%B6%D5%A5%D6%80_1045/')
# print(r)
soup = BeautifulSoup(''.join(doc))
f = open('some1.txt', 'w')
f.write(soup.text)

f.close()
