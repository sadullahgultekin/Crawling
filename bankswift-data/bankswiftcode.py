import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import requests
import json
import re

base_link = "https://www.bankswiftcode.org"

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(options=options)

driver.get(base_link)

all_letter_links = []
i = 1
while True:
    try:
        all_letter_links.append(driver.find_element_by_xpath('//*[@id="breadcrumbs"]/li['+str(i)+']/a').get_attribute("href"))
    except Exception as e:
        break
    i += 1

all_data = {}
will_pass = False

for letter_link in all_letter_links:
    page = requests.get(letter_link).text
    all_country_links = re.findall(r'<td><a href="(.*)">(.*)</a>', page)
    for country_link_and_name in all_country_links:
        if "alignnone" in country_link_and_name[1]:
            continue
        
        print(country_link_and_name[1])
        country_link = base_link + country_link_and_name[0]
        page = requests.get(country_link).text
        matches = re.findall(r"<td>(.*)<\/td>\n<td>(.*)<\/td>\n<td>(.*)<\/td>\n<td>(.*)<\/td>\n<td>(.*)<\/td>", page)
        
        data_for_country = []
        print(matches)
        for m in matches[1:]:
            data_for_country.append({
                'No': m[0],
                'Bank or Institution': m[1],
                'City': m[2],
                'Branch Name': m[3],
                'Swift Code': m[4]
            })
        all_data[country_link_and_name[1]] = data_for_country

driver.close()

with open("all_swiftbank_data.json", "w") as f:
    f.write(json.dumps(all_data))

