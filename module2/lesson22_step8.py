from selenium import webdriver
import time
import os

import os

current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_name("firstname")
    input1.send_keys("firstname")

    input2 = browser.find_element_by_name("lastname")
    input2.send_keys("lastname")

    input3 = browser.find_element_by_name("email")
    input3.send_keys("email")

    button1 = browser.find_element_by_id("file")
    button1.send_keys(file_path)

    button2 = browser.find_element_by_css_selector("[type='submit']")
    button2.click()

    # Ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()