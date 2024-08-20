from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def test_chrome():
#1. Открыть страницу по ссылке
    chrome.get('http://the-internet.herokuapp.com/inputs')
#2. Введите в поле текст 1000
    input_field = chrome.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_field.send_keys("1000")
    sleep(2)
#3. Очистите это поле
    input_field.clear()
#4. Введите в это же поле текст 999
    input_field.send_keys("999")
    sleep(2)


def test_firefox():
#1. Открыть страницу по ссылке
    firefox.get('http://the-internet.herokuapp.com/inputs')
#2. Введите в поле текст 1000
    input_field = firefox.find_element(By.CSS_SELECTOR, "input[type='number']")
    input_field.send_keys("1000")
    sleep(2)
#3. Очистите это поле
    input_field.clear()
#4. Введите в это же поле текст 999
    input_field.send_keys("999")
    sleep(2)

test_chrome()
chrome.quit()

test_firefox()
firefox.quit()