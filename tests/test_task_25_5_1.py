import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# путь: python -m pytest -v --driver Chrome --driver-path tests/chromedriver.exe tests/test_task_25_5_1.py

@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome(executable_path=r'C:\PycharmProjects\pythonProject4PetFriends\tests\chromedriver.exe')
   # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()

def test_show_all_pets():
   # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('adenisov.pro@gmail.com')
   # Вводим пароль.
    pytest.driver.find_element_by_id('pass').send_keys('Andrey67')
   # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что мы оказались на главной странице пользователя
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"


def test_attributes():
    pytest.driver = webdriver.Chrome(
      executable_path=r'C:\PycharmProjects\pythonProject4PetFriends\tests\chromedriver.exe')
    pytest.driver.get('http://petfriends1.herokuapp.com/all_pets')
    images = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-img-top')))
    names = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-title')))
    descriptions = WebDriverWait(pytest.driver, 10).until(
      EC.presence_of_element_located((By.CSS_SELECTOR, '.card-deck .card-text')))
    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0

# проверка по заданию 25.3.1
def test_my_pets():
    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('adenisov.pro@gmail.com')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Andrey67')
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
    # Заходим на страницу своих питомцев
    pytest.driver.find_element_by_css_selector("div#navbarNav > ul > li > a").click()

    assert pytest.driver.find_element_by_tag_name('h2').text == "Andrey Denisov"
    # Выбираем моих питомцев
    del_pet = pytest.driver.find_elements_by_xpath('//td[@class="smart_cell"]')
    # Выбираем все элементы фотографий питомцев
    images = pytest.driver.find_elements_by_xpath('//th/img')
    # Назначаем переменную для подсчёта количества питомцев с фотографией
    photo_presence = 0
    pytest.driver.implicitly_wait(10)
    # Через проверку у всех питомцев, что attribute 'src' не пустое значение, определяем
    # количество питомцев с фотографией
    for i in range(len(del_pet)):
      if images[i].get_attribute('src') != '':
         photo_presence += 1
      else:
         photo_presence = photo_presence
    # Проверяем, что половина всех питомцев имеет фотографию
    assert photo_presence >= (len(del_pet) / 2)
   # У всех питомцев есть имя, возраст и порода.
    assert pytest.driver.find_element_by_xpath(
      '//*[@id="all_my_pets"]/table/tbody/tr[1]' and '//*[@id="all_my_pets"]/table/tbody/tr[2]' and '//*[@id="all_my_pets"]/table/tbody/tr[3]').text != ''
   # У всех питомцев разные имена, породы и возраст.
    Name_breed_age1 = pytest.driver.find_element_by_xpath(
      '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[1]' and '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[2]' and '//*[@id="all_my_pets"]/table/tbody/tr[1]/td[3]')
    Name_breed_age2 = pytest.driver.find_element_by_xpath(
      '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[1]' and '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[2]' and '//*[@id="all_my_pets"]/table/tbody/tr[2]/td[3]')
    Name_breed_age3 = pytest.driver.find_element_by_xpath(
      '//*[@id="all_my_pets"]/table/tbody/tr[3]/td[1]' and '//*[@id="all_my_pets"]/table/tbody/tr[3]/td[2]' and '//*[@id="all_my_pets"]/table/tbody/tr[3]/td[3]')
    assert Name_breed_age1 != Name_breed_age2 != Name_breed_age3




