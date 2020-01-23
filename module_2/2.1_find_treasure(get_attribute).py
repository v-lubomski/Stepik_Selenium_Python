from selenium import webdriver
import time
import math

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/get_attribute.html'


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    time.sleep(1)
    # получаем значение valuex и вычисляем у
    treasure = browser.find_element_by_id('treasure')
    valuex = treasure.get_attribute('valuex')
    y = calc(valuex)
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
