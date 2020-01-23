import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()

try:
    # Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
    browser.get("https://portal.i-sys.ru/sites/bp/Lists/List32/NewForm.aspx")
    time.sleep(20)
    browser.get("https://portal.i-sys.ru/sites/bp/Lists/List32/view.aspx")
    time.sleep(5)
    browser.get("https://portal.i-sys.ru/sites/bp/Lists/List32/NewForm.aspx")
    time.sleep(5)


finally:
    browser.quit()
