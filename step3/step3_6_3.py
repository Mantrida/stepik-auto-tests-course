import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

@pytest.mark.parametrize('number', ['236895', '236896', '236897', '236898', '236899', '236903', '236904', '236905'])
def test_guest_should_see_login_link(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"

    browser.implicitly_wait(5)

    browser.get(link)

    cookie_session = {'name': 'sessionid', 'value': 'hw6v71j0r5dxmflork8nx6x312945hz0'}
    cookie_token = {'name': 'csrftoken', 'value': 'PWooZtjP5KhCcipLRtmwTGtFwXFLxfUkyR5Pfglx6moewRzyQYmPepwS1mFotnN5'}  # где sessionid и csrftoken - ваши куки.

    browser.add_cookie(cookie_session)
    browser.add_cookie(cookie_token)

    browser.get(link)

    textarea = browser.find_element_by_css_selector(".textarea")

    answer = math.log(int(time.time()))
    print(answer)

    textarea.send_keys(str(answer))

    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()

    message = browser.find_element_by_css_selector(".smart-hints__hint")

    assert "Correct!" == message.text, print(message.text)

    time.sleep(1)

    # The owls are not what they seem! OvO