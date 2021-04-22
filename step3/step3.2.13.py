from selenium import webdriver
import time

def test1():
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

        # Заполнение обязательных полей формы
    element1 = browser.find_element_by_css_selector('.first_block .first')
    element1.send_keys("Ivan")

    element2 = browser.find_element_by_css_selector('.first_block .second')
    element2.send_keys("Ivanov")

    element3 = browser.find_element_by_css_selector('.first_block .third')
    element3.send_keys("ivan@mail.ru")

        # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element_by_tag_name("h1")
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text, 'Ошибка регистрации'