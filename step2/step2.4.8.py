from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    wait = WebDriverWait(browser, 30)

    wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    button = browser.find_element_by_id("book")
    button.click()

    x_element = browser.find_element_by_id('input_value').text
    y = calc(x_element)
    print(y)

    element1 = browser.find_element_by_id('answer')
    element1.send_keys(y)

    button = browser.find_element_by_id("solve")
    button.click()

finally:
    time.sleep(20)
    browser.quit()