from selenium import webdriver
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Заполнение обязательных полей формы
    element1 = browser.find_element_by_name('firstname')
    element1.send_keys("Ivan")

    element2 = browser.find_element_by_name('lastname')
    element2.send_keys("Ivanov")

    element3 = browser.find_element_by_name('email')
    element3.send_keys("ivan@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла

    element4 = browser.find_element_by_id('file')
    element4.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()
