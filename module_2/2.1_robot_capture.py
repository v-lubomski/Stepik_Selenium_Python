from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/math.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    # получаем значение переменной х и вычисляем у
    x_el = browser.find_element_by_id('input_value')
    x = x_el.text
    y = calc(x)
    # находим поле и вставляем ответ
    input_for_answer = browser.find_element_by_id('answer')
    input_for_answer.send_keys(y)
    # отмечаем радиобаттон и чекбокс и жмём кнопку отправки формы
    browser.find_element_by_id('robotCheckbox').click()
    browser.find_element_by_id('robotsRule').click()
    browser.find_element_by_css_selector('button.btn').click()
    # выводим текст всплывшего окна в консоль
    print(browser.switch_to.alert.text)

finally:
    browser.quit()


