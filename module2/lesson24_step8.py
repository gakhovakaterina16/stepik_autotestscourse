from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    y = str(math.log(abs(12*math.sin(int(x)))))
    return y


try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button1 = browser.find_element(By.ID, "book")
    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    button1.click()

    button2 = browser.find_element(By.ID, "solve")

    x = browser.find_element(By.ID, "input_value").text
    browser.execute_script("return arguments[0].scrollIntoView(true);", button2)
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(calc(x))


    button2.click()

    # Ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()