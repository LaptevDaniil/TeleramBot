from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time

webdriver = "C:\msedgedriver.exe"
browser = Edge(webdriver)

browser.get("https://vkusnoitochka.ru/menu")

XPATH_INFO = '//*[@id="product-632c1f06e71194662c7415a3"]'
#XPATH_MENU = '//*[@id="category_5dfcb0c0ac65eaba25f77815"]'
elementsInfo = browser.find_elements(by=By.XPATH, value=XPATH_INFO)
#elementsMenu = browser.find_elements(by=By.XPATH, value=XPATH_MENU)

className = elementsInfo[0].get_attribute("class")
#classMenu = elementsInfo[0].get_attribute("class")

infos = []
menuClasses = []

menus = []

menus = browser.find_elements(by=By.CSS_SELECTOR, value=f"li[class='menu-categories__item']")
print(menus)

# print(len(infos))

for menu in menus:
    menu.click()
    infos.append(i for i in browser.find_elements(by=By.CSS_SELECTOR, value=f"li[class='{className}']"))

for info in infos:
    if info.text.split('\n')[0].find(info.text.split('\n')[1]) > 0:
        print(info.text.split('\n')[0] + " " + info.text.split('\n')[-1].replace(" ₽", "₽"))
    else:
        print(info.text.replace("\n", " ").replace(" ₽", "₽"))

time.sleep(1)
browser.close()
