from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from math import log, sin


# функция вычисления капчи
def calc(val):
    return str(log(abs(12*sin(int(val)))))


# задаём ссылку и открываем браузер
link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    # открываем страницу
    browser.get(link)

    # ждём, когда цена опустится до 100 и жмём кнопку Book
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element_by_id('book').click()

    # находим х и считаем уравнение капчи
    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    # вставляем результат в поле, жмём на кнопку отправки формы
    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_id('solve').click()

    # выводим из алерта в консоль ответ на задание
    print(browser.switch_to.alert.text)

finally:
    # завершаем все процессы вебдрайвера
    browser.quit()
