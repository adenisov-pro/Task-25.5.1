import pytest
from selenium import webdriver
driver=webdriver.Chrome(executable_path=r'C:\Users\Frameholder\Downloads\chromedriver_win32\chromedriver.exe')
from telnetlib import EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#  python -m pytest -v  test_show_my_pets.py  прописываем в терминал

@pytest.fixture(autouse=True)
def testing():
   pytest.driver = webdriver.Chrome(executable_path=r'C:\Users\Frameholder\Downloads\chromedriver_win32\chromedriver.exe')
   # Переходим на страницу авторизации
   pytest.driver.get('http://petfriends1.herokuapp.com/login')

   yield

   pytest.driver.quit()


def test_show_all_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('alborzdy@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('1111')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Проверяем, что попали на нужную страницу
   assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"

def test_attributes():
   pytest.driver.get('http://petfriends1.herokuapp.com/all_pets')
   images = pytest.driver.find_elements_by_css_selector('.card-deck .card-img-top')
   names = pytest.driver.find_elements_by_css_selector('.card-deck .card-title')
   descriptions = pytest.driver.find_elements_by_css_selector('.card-deck .card-text')
   #Вопрос к ментору - почему тест валится, если прописывать ожидание - где ошибка?
   #images = WebDriverWait(driver, 10).until(EC.presence_of_elements_located((By.CSS_SELECTOR,'.card-deck .card-img-top')))
   #names = WebDriverWait(driver, 10).until(EC.presence_of_elements_located((By.CSS_SELECTOR,'.card-deck .card-title')))
   #descriptions = WebDriverWait(driver, 10).until(EC.presence_of_elements_located((By.CSS_SELECTOR,'.card-deck .card-text')))

   for i in range(len(names)):
      assert images[i].get_attribute('src')!=''
      assert names[i].text !=''
      assert descriptions[i].text!=''
      assert ', ' in descriptions[i]
      parts = descriptions[i].text.split(", ")
      assert len(parts[0]) > 0
      assert len(parts[1]) > 0


#тестируем своих питомцев на то что более половины питомцев с фото, на присутствие всех данных и на то что эти данные отличаются друг от друга
def test_my_pets():
   # Вводим email
   pytest.driver.find_element_by_id('email').send_keys('alborzdy@gmail.com')
   # Вводим пароль
   pytest.driver.find_element_by_id('pass').send_keys('1111')
   # Нажимаем на кнопку входа в аккаунт
   pytest.driver.find_element_by_css_selector('button[type="submit"]').click()
   # Заходим на страницу своих питомцев
   pytest.driver.find_element_by_css_selector("div#navbarNav > ul > li > a").click()

   assert pytest.driver.find_element_by_tag_name('h2').text == "Yaraslau Borzdy"
   # Выбираем моих питомцев локатором кнопки удаления животного
   del_pet = pytest.driver.find_elements_by_xpath('//td[@class="smart_cell"]')
   # Выбираем все элементы фотографий питомцев пользователя
   images = pytest.driver.find_elements_by_xpath('//th/img')
   # Назначаем переменную для подсчёта количества питомцев пользователя с фотографией
   photo_presence = 0
   driver.implicitly_wait(5)
   # Через проверку у всех питомцев, что attribute 'src' не пустое значение, определяем
   # количество питомцев с фотографией
   for i in range(len(del_pet)):
      if images[i].get_attribute('src') != '':
         photo_presence += 1
      else:
         photo_presence = photo_presence
   # Проверяем, что как min половина всех питомцев имеет фотографию
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
