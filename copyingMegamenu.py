from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging
import unittest
import time
# import random
import requests
# import csv



class CopyingMegamenu(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("https://ru.sas.am")
        driver.maximize_window()
        time.sleep(3)
        elem = driver.find_element_by_xpath("//div[@class='sidenav']/div[1]/ul[1]/li")
        ActionChains(driver).move_to_element(elem).click().perform()
        time.sleep(3)
        qty = 1 + len(driver.find_elements_by_xpath("//div[@class='main-menu-wrp']/ul/li"))
        n = 1
        file = open("./csv/megamenu_ru.cvs","w")
        file.write("name_category" + ',' + "img_category" + ',' + "url_category" +','+ "title" '\n')
        while n < qty:
            xpath = "//div[@class='main-menu-wrp']/ul/li[" + str(n) + "]"
            elem = driver.find_element_by_xpath(xpath)
            ActionChains(driver).move_to_element(elem).click().perform()
            time.sleep(3)
            img = driver.find_element_by_xpath(xpath + "/div[1]/span/img")
            element = driver.find_element_by_xpath(xpath + "/div[2]/a")
            img_category = self.copying_img(img.get_attribute("src"))
            name_category = img.get_attribute("title")
            url_category = element.get_attribute("href")
            qty_div = len(driver.find_elements_by_xpath(xpath + "/div[2]/div[2]/div"))
            print('qty_div = '+str(qty_div))
            file.write(name_category + ',' + img_category + ',' + url_category +',' + "True" + '\n')
            i = 1
            while i < qty_div:
                xpath_column = xpath + "/div[2]/div[2]/div["+ str(i) +"]/ul/li"
                qty_li = 1 + len(driver.find_elements_by_xpath(xpath_column))
                c = 1
                while c < qty_li:
                    xpath_a = xpath_column + "["+ str(c) +"]/a"
                    elem_categoty = driver.find_element_by_xpath(xpath_a)
                    url_img = "https://www.sas.am" + elem_categoty.get_attribute("rel")
                    img_category = self.copying_img(url_img)
                    name_category = elem_categoty.text
                    url_category = elem_categoty.get_attribute("href")
                    title = driver.find_element_by_xpath(xpath_column + "["+ str(c) +"]").get_attribute("class")
                    if title == " title":
                         title = "True"
                    else:
                         title = "False"
                    file.write(name_category + ',' + img_category + ',' + url_category + ','+ str(title) +'\n')
                    print("c ="+str(c))
                    c = c + 1
                print('i = '+str(i))
                i = i + 1
            ActionChains(driver).move_to_element(elem).click().perform()
            n = n + 1
            print("n = "+str(n))
        file.close()

    def copying_img(self, url):
        p = requests.get(url)
        name = url.split("/", -1)
        out = open("./qwe/"+name[-1]+"", "wb")
        out.write(p.content)
        out.close()
        return name[-1]

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
