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
    chrome.get('http://the-internet.herokuapp.com/login')
#2. В поле username введите значение tomsmith
    input_field = chrome.find_element(By.CSS_SELECTOR, "input[id='username']")
    input_field.send_keys("tomsmith")
    sleep(2)
#3. В поле password введите значение SuperSecretPassword!
    input_field = chrome.find_element(By.CSS_SELECTOR, "input[id='password']")
    input_field.send_keys("SuperSecretPassword!")
    sleep(2)
#4. Нажмите кнопку Login
    add_button = chrome.find_element(By.CSS_SELECTOR, "button[type='submit']")
    add_button.click()
    sleep(3)



def test_firefox():
#1. Открыть страницу по ссылке
    firefox.get('http://the-internet.herokuapp.com/login')
#2. В поле username введите значение tomsmith
    input_field = firefox.find_element(By.CSS_SELECTOR, "input[id='username']")
    input_field.send_keys("tomsmith")
    sleep(2)
#3. В поле password введите значение SuperSecretPassword!
    input_field = firefox.find_element(By.CSS_SELECTOR, "input[id='password']")
    input_field.send_keys("SuperSecretPassword!")
    sleep(2)
#4. Нажмите кнопку Login
    add_button = firefox.find_element(By.CSS_SELECTOR, "button[type='submit']")
    add_button.click()
    sleep(3)

test_chrome()
chrome.quit()

test_firefox()
firefox.quit()