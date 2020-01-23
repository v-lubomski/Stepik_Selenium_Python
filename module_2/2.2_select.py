from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/selects1.html'

try:
    browser.get(link)
    sleep(1)

    num1 = browser.find_element_by_id('num1').text
    num2 = browser.find_element_by_id('num2').text
    result = int(num1) + int(num2)

    select = Select(browser.find_element_by_id('dropdown'))
    select.select_by_visible_text(str(result))
    browser.find_element_by_css_selector('.btn.btn-default').click()

    print(browser.switch_to.alert.text)

finally:
    browser.quit()


