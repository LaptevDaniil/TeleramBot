from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time

webdriver = "C:\msedgedriver.exe"
browser = Edge(webdriver)

browser.get("https://dodopizza.ru/dubna")

XPATH_INFO = '//*[@id="pizzas"]/article'
elementsInfo = browser.find_elements(by=By.XPATH, value=XPATH_INFO)

className = elementsInfo[0].get_attribute("class")

infos = browser.find_elements(by=By.CSS_SELECTOR, value=f"article[class='{className}']")
arr_dodo = []

for info in infos:
    arr_dodo.append(info.text.split('\n')[0] + " " + info.text.split('\n')[-2])

time.sleep(1)
browser.close()