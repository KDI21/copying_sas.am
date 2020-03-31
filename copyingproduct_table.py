# import csv
import requests
import re
from bs4 import BeautifulSoup


import csv
class CopyingProductTable(object):
    """docstring for CopyingProductTable."""

    def copying_product_table(file_obj):
        reader = csv.DictReader(file_obj, delimiter=';')
        sas = "https://en.sas.am"
        eror = open("csv/eror.csv", 'w')
        file = open("csv/product_list_en.csv","w")
        file.write('name_product' + ';' + 'product_code' +';'+'product_id' +';' + 'price' + ';' + 'price_before_discount' + ';' + 'img_product' + ';' + 'description' + ';' + 'details' + ';' + 'structure' + ';' +'storage_method' + '\n')
        copying = Qwe()
        for line in reader:
            print(line['url_product'])
            doc  = requests.get(line["url_product"])
            # doc  = requests.get('https://en.sas.am/products/Crab_Borrelli_Mare_in_oil_17319/')
            soup = BeautifulSoup(''.join(doc.text), features = "lxml")
            warning404 = soup.find('h1')
            if warning404 == None :
                i = 0
                name_product = soup.find('td', {"class"  : "text"}).find('h2').find('b').text
                elem = soup.find('table', {"class" : "ingrid"}).find_all('tr')
                details = []
                while i < len(elem):
                    if elem[i].find('td').text == "Код товара" or elem[i].find('td').text == "Ապրանքի կոդը" or elem[i].find('td').text == "Product code":
                        product_code =elem[i].find_all('td')[1].text
                        i = i + 1
                        product_id = elem[i].find_all('td')[1].text
                        i = i - 1
                    key = elem[i].find_all('td')[0].text
                    value = elem[i].find_all('td')[1].text
                    details.append({key : value})
                    i = i + 1
                price = re.sub("\D", "", soup.find('strong', {"class" : "priceValue"}).text)
                elem = soup.find('li', {"class" :"price normal-price clearfix" }).find('div')
                price_before_discount = None
                if elem != None:
                    price_before_discount = re.sub("\D", "", elem.text)
                url =  sas + soup.find('table', {"class" : "product card-prod"}).find('img')['src']
                img_product = copying.copying_img(url)
                elem = soup.find('table',{"class" : "product card-prod"}).find_all('tr')[2].find('td').find('p')
                print(elem)
                if elem != None:
                    elem = elem.text
                    description = elem.split(":",)[-1].split("\n")
                    description = ''.join(description)
                else:
                    description = "no description"
                elem = soup.find_all('div', {"class" : "overflow details"})
                if len(elem) > 3:
                    print(line['url_product'])
                    assert 1 != 1
                i = 1
                structure = []
                storage_method = 'None'
                while i < len(elem):
                    element = elem[i].find('div', {"class" : "items"})
                    if element != None:
                        element = elem[i].find('div', {"class" : "items"}).find_all('div')
                        n = 0
                        structure = []
                        while  n < len(element):
                            key = element[n].find('h5').text
                            value = element[n].find('strong').text
                            structure.append({key : value})
                            n = n + 1
                    else:
                        storage_method = str(elem[i].text).split('\n')[-1]
                    i = i + 1
                print(name_product + ';' + str(product_code) + ';' + str(product_id) + ';' + str(price) + ';' + str(price_before_discount) + ';' + img_product + ';' + str(description) + ';' + str(details) +';' + str(structure) + ';' +storage_method +'\n')
                file.write(name_product + ';' + str(product_code) + ';' + str(product_id) + ';' + str(price) + ';' + str(price_before_discount) + ';' + img_product + ';' + str(description) + ';' + str(details) +';' + str(structure) + ';' +storage_method +'\n')
            else:
                eror.write(line['url_product'])

class Qwe(object):
    def copying_img(self, url):
        p = requests.get(url)
        name = url.split("/", -1)
        out = open("./img_product/"+name[-1]+"", "wb")
        out.write(p.content)
        out.close()
        return name[-1]



if __name__ == "__main__":
    with open("./csv/product_item_en_one to one.csv") as f_obj:
        CopyingProductTable.copying_product_table(f_obj)
