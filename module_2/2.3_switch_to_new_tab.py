from selenium import webdriver
from math import log, sin
from time import sleep


# функция вычисления капчи
def calc(val):
    return str(log(abs(12*sin(int(val)))))


# задаём ссылку и открываем браузер
link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()

try:
    # открываем страницу, кликаем на кнопку
    browser.get(link)
    browser.find_element_by_css_selector('.btn-primary').click()

    # переключаемся на новую вкладку
    second_window = browser.window_handles[1]
    browser.switch_to.window(second_window)

    # находим х и считаем уравнение капчи
    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    # вставляем результат в поле, жмём на кнопку отправки формы
    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_tag_name('button').click()

    # выводим из алерта в консоль ответ на задание
    print(browser.switch_to.alert.text)


finally:
    # завершаем все процессы вебдрайвера
    browser.quit()
