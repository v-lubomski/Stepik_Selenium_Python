from selenium import webdriver
from time import sleep
from math import log, sin

link = 'http://suninjuly.github.io/alert_accept.html'
browser = webdriver.Chrome()


def calc(val):
    return str(log(abs(12 * sin(int(val)))))


try:
    browser.get(link)
    sleep(1)

    browser.find_element_by_css_selector('.btn.btn-primary').click()
    browser.switch_to.alert.accept()
    sleep(1)

    x = browser.find_element_by_id('input_value').text
    result = calc(x)

    browser.find_element_by_id('answer').send_keys(result)
    browser.find_element_by_tag_name('button').click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()
