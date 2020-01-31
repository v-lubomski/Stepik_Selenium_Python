from selenium import webdriver
import unittest


def fill_form(link):
    browser.get(link)
    browser.find_element_by_xpath('//label[contains(text(), "First name")]/following-sibling::input').send_keys('Влад')
    browser.find_element_by_xpath('//label[contains(text(), "Last name")]/following-sibling::input').send_keys('Ли')
    browser.find_element_by_xpath('//label[contains(text(), "Email")]/following-sibling::input').send_keys('sf@dsa.ru')
    browser.find_element_by_css_selector("button.btn").click()
    return browser.find_element_by_tag_name("h1").text


class TestReg(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration1.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(fill_form("http://suninjuly.github.io/registration2.html"),
                         "Congratulations! You have successfully registered!", "registration is failed")


if __name__ == "__main__":
    browser = webdriver.Chrome()
    try:
        unittest.main()
    finally:
        browser.quit()
