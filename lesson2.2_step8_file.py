import os
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
file_name = "file_example.txt"
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("email")
    browser.find_element(By.CSS_SELECTOR, "[type='file']").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn").click()
finally:
    time.sleep(10)
    browser.quit()
