import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(options=options)

with open("all_codes.txt","r") as fp:
    all_codes = fp.read().splitlines()

all_data = []

for idx, code in enumerate(all_codes):
    print('current code:', code)
    driver.get("https://www.bic-code.org/container-bic-code/"+code)
    i = 0
    one_data = {}
    while True:
        i += 1
        try:
            key = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr['+str(i)+']/th').text
            value = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr['+str(i)+']/td').text
            print(key, value)
            one_data[key] = value
        except Exception as e:
            print(e)
            break
    all_data.append(one_data)

driver.close()

with open("all_bic_data.json", "w") as f:
    f.write(json.dumps(all_data))


