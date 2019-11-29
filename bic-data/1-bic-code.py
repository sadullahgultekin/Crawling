import sys
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')

driver = webdriver.Chrome(options=options)

f = open("all_codes.txt", "w")

not_leave = True
page_num = 1

while(not_leave):
    print("page number is", page_num)
    driver.get("https://www.bic-code.org/bic-letter-search/?resultsperpage=500&cpage="+str(page_num))
    for i in range(3,503):
        try:
            code = driver.find_element_by_xpath('//*[@id="wrapper"]/div[2]/div[3]/div[2]/div/div/div[2]/table/tbody/tr['+ str(i) +']/td[1]').text
            f.write(code+"\n")
            print(code)
        except Exception as e:
            print(e)
            not_leave = False
            break
    page_num += 1


f.close()

driver.close()

