from selenium import webdriver
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element_by_xpath('//label[contains(text(), "First name")]/following-sibling::input').send_keys('Влад')
    browser.find_element_by_xpath('//label[contains(text(), "Last name")]/following-sibling::input').send_keys('Ли')
    browser.find_element_by_xpath('//label[contains(text(), "Email")]/following-sibling::input').send_keys('sf@dsa.ru')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Registration not succeed'

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
