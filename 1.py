
import requests
r = requests.get('https://www.sas.am')
f = open('some.txt', 'w')
print(r)
f.write(r.text)
f.close()
