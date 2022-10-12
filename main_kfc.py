from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time

webdriver = "C:\msedgedriver.exe"
browser = Edge(webdriver)

browser.get("https://www.kfc.ru")

XPATH_INFO = '//*[@id="main1004841"]/div/div[2]/a[6]'
elementsInfo = browser.find_elements(by=By.XPATH, value=XPATH_INFO)

className = elementsInfo[0].get_attribute("class")

infos = browser.find_elements(by=By.CSS_SELECTOR, value=f"a[class='{className}']")
arr_kfc = []

for info in infos:
    if info.text.split('\n')[1] != 'Будет позже':
        arr_kfc.append(info.text.replace("\n", " ").replace(" ₽", "₽"))

time.sleep(1)
browser.close()
