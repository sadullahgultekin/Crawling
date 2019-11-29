import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
import time 

options = webdriver.ChromeOptions()
#options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(options=options)
driver.get("https://www.iban.org/bic.html")

selectCountry = Select(driver.find_element_by_css_selector('.choose-country.form-control'))
selectBank = Select(driver.find_element_by_css_selector('.choose-bank.form-control'))
selectSwift = Select(driver.find_element_by_css_selector('.choose-swift.form-control'))

i = 0
while True:
    try:
        selectCountry.select_by_index(i)
    except:
        break
    i += 1

    time.sleep(3)    

    j = 0
    while True:
        try:
            selectBank.select_by_index(j)
        except:
            break
        j += 1
        
        time.sleep(3)

        k = 0
        while True:
            try:
                selectSwift.select_by_index(k)
            except:
                break
            k += 1

            time.sleep(3)

