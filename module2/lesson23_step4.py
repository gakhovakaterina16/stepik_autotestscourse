from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By

def calc(x):
    y = str(math.log(abs(12*math.sin(int(x)))))
    return y


try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.CSS_SELECTOR, "[type='submit']")
    button1.click()

    browser.switch_to.alert.accept()

    x = browser.find_element(By.ID, "input_value").text
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))

    button2 = browser.find_element(By.CLASS_NAME, "btn.btn-primary")
    button2.click()


    # Ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()