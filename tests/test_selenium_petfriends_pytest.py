#!/usr/bin/python3
# -*- encoding=utf8 -*-

# Вы можете найти очень простой пример использования Selenium с PyTest в этом файле.
#
# More info about pytest-selenium:
#    https://pytest-selenium.readthedocs.io/en/latest/user_guide.html
#
# How to run:
#  1) Download geko driver for Chrome here (Скачать драйвер geko для Chrome можно здесь):
#     https://chromedriver.storage.googleapis.com/index.html?path=2.43/
#  2) Install all requirements (Установите все требования):
#     pip install -r requirements.txt
#  3) Run tests (Запускайте тесты):
#     python3 -m pytest -v --driver Chrome --driver-path /tests/chrome test_selenium_simple.py
#
import time

def test_search_example(selenium):
    """ Search some phrase in google and make a screenshot of the page. """
# Найдите какую-нибудь фразу в Google и сделайте скриншот страницы
    # Open google search page (Откройте страницу поиска Google):
    selenium.get('https://google.com')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!
                   # только для демонстрационных целей, не повторяйте это на реальных проектах!
    # Find the field for search text input (Найдите поле для ввода текста поиска):
    search_input = selenium.find_element_by_name('q')


    # Enter the text for search (Введите текст для поиска):
    search_input.clear()
    search_input.send_keys('first test')

    time.sleep(5)  # just for demo purposes, do NOT repeat it on real projects!

    # Click Search (Нажмите кнопку Поиск):
    search_button = selenium.find_element_by_name('btnK')
    search_button.submit()

    time.sleep(10)  # just for demo purposes, do NOT repeat it on real projects!

    # Make the screenshot of browser window (Сделайте скриншот окна браузера):
    selenium.save_screenshot('result.png')

    # путь: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_selenium_petfriends_pytest.py
