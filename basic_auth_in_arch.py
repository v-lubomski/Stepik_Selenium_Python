import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(5)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("http://v.lyubomskiy@i-sys100500!!!!!!!:bznt-arch.i-sys.ru:777/")
time.sleep(5)


ch_opts = webdriver.ChromeOptions()
ch_opts.add_argument(f"--load-extension={ui_config['pages_config']['chrome_extension']}")
driver = webdriver.Chrome()
