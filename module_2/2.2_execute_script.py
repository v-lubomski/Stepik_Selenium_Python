from selenium import webdriver
import math
from time import sleep

browser = webdriver.Chrome()
link = "https://SunInJuly.github.io/execute_script.html"


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))


try:
    browser.get(link)
    sleep(1)

    # вычисления
    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    # находим инпуты
    answer = browser.find_element_by_id('answer')
    checkbox = browser.find_element_by_id('robotCheckbox')
    radio = browser.find_element_by_id('robotsRule')
    button = browser.find_element_by_css_selector('.btn.btn-primary')

    # скроллим до поля ввода
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    sleep(1)

    # заполняем, отмечаем, подтверждаем
    answer.send_keys(result)
    checkbox.click()
    radio.click()
    button.click()

    # вывод алерта в консоль
    print(browser.switch_to.alert.text)

finally:
    browser.quit()

