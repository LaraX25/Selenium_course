from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    a = browser.find_element(By.ID, "num1").text
    b = browser.find_element(By.ID, "num2").text
    c = str(int(a) + int(b))
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(c)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(10)
    browser.quit()
