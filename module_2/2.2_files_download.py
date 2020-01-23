import os
from time import sleep
from selenium import webdriver

browser = webdriver.Chrome()

try:
    browser.get('http://suninjuly.github.io/file_input.html')
    sleep(1)

    # находим все инпуты на странице
    firstname_input = browser.find_element_by_css_selector('[name="firstname"]')
    lastname_input = browser.find_element_by_css_selector('[name="lastname"]')
    email_input = browser.find_element_by_css_selector('[name="email"]')
    file_input = browser.find_element_by_id('file')
    button = browser.find_element_by_css_selector('.btn.btn-primary')

    # находим путь до файла, который будем загружать
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    # заполняем поля, загружаем файл, нажимаем на кнопку отправки формы
    firstname_input.send_keys('Имя имя имечко')
    lastname_input.send_keys('Фамилия фамилия фамилечко')
    email_input.send_keys('email@email.emailichek')
    file_input.send_keys(file_path)
    button.click()

    # выводим код алерта в консоль
    print(browser.switch_to.alert.text)

finally:
    browser.quit()

