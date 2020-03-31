import csv
import requests
import re
from bs4 import BeautifulSoup

class CopyingProductTable(object):
    """docstring for CopyingProductTable."""


    def copying_product_table(file_obj):
        reader = csv.DictReader(file_obj, delimiter=';')
        sas = "https://ru.sas.am"
        file = open("csv/product_item_ru_many to many.csv","w")
        file.write('name_category' + ';' + 'img_product'+';'+ 'name_product'+';'+ 'url_product'+ '\n')
        file_singl = open("csv/product_item_ru_one to one.csv","w")
        file_singl.write('name_category' + ';' + 'img_product'+';'+ 'name_product'+';'+ 'url_product'+ '\n')
        copying = Qwe()
        for line in reader:
            doc  = requests.get(line["url_category"])
            soup = BeautifulSoup(''.join(doc.text), features = "lxml")
            soup.prettify()
            tabte_product = soup.find(attrs = {"class" : "table"})
            if tabte_product != None:
                n = False
                name_category = line["name_category"]
                while n != True:
                    tabte_product = soup.find(attrs = {"class" : "table"})
                    product_item = tabte_product.find_all(attrs = {"class" : "td-overally"})
                    c = 0
                    print(len(product_item))
                    while c <len(product_item):
                        item = product_item[c].find('h3').find('a')
                        name_product = item.text
                        url_product =sas + item['href']
                        qwe = product_item[c].find('a').find('img')
                        url_img = sas +qwe['src']
                        img_product = copying.copying_img(url_img)
                        file.write(name_category + ';' + img_product + ';' + name_product + ';' + url_product + '\n')
                        csv_file = csv.reader(open('csv/product_item_en_one to one.csv', 'r'), delimiter = ';')
                        qty = True
                        for row in csv_file:
                            if str(url_product) == str(row[-1]):
                                qty = False
                        if qty == True:
                            file_singl.write(name_category + ';' + img_product + ';' + name_product + ';' + url_product + '\n')

                        c = c + 1
                    print(c)
                    elem = tabte_product.find('a', {"class" : "next history_filter_paging_el" })
                    if elem != None:
                        href = sas + elem['href']
                        doc  = requests.get(href)
                        soup = BeautifulSoup(doc.text, features="lxml")
                        soup.prettify()
                    else:
                        n = True
        file.close()
        file_singl.close()



            # assert 1 != 1



class Qwe(object):
    def copying_img(self, url):
        p = requests.get(url)
        name = url.split("/", -1)
        out = open("./img/"+name[-1]+"", "wb")
        out.write(p.content)
        out.close()
        return name[-1]



if __name__ == "__main__":
    with open("./csv/megamenu_ru.csv") as f_obj:
        CopyingProductTable.copying_product_table(f_obj)
