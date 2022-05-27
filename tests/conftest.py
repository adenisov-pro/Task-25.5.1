import pytest
import uuid


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    # This function helps to detect that some test failed
    # (Эта функция помогает обнаружить, что какой-то тест не пройден)
    # and pass this information to teardown: (и передать эту информацию в демонтаж)

    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture
def web_browser(request, selenium):

    browser = selenium
    browser.set_window_size(1400, 1000)
    # задаем размер окна

    # Return browser instance to test case (Вернуть экземпляр браузера в тестовый пример):
    yield browser

    # Do teardown (this code will be executed after each test)
    # (сделать разрыв: этот код будет выполняться после каждого теста):

    if request.node.rep_call.failed:
        # Make the screen-shot if test failed(сделайте снимок экрана, если тест не пройден):
        try:
            browser.execute_script("document.body.bgColor = 'white';")

            # Make screen-shot for local debug (сделать скриншот для локальной отладки):
            browser.save_screenshot('screenshots/' + str(uuid.uuid4()) + '.png')

            # For happy debugging (для счастливой отладки):
            print('URL: ', browser.current_url)
            print('Browser logs:')
            for log in browser.get_log('browser'):
                print(log)

        except:
            pass # just ignore any errors here (просто игнорируйте любые ошибки здесь)


from datetime import datetime # определяем время прохождения теста
@pytest.fixture(autouse=True)
def time_delta():
    start_time = datetime.now()
    yield
    end_time = datetime.now()
    print (f"\nТест шел: {end_time - start_time}")
