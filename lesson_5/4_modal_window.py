from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#CHROME
with webdriver.Chrome() as chrome:
#1. Открыть страницу по ссылке
    chrome.get('http://the-internet.herokuapp.com/entry_ad')
#2. Открытие модального окна
    wait = WebDriverWait(chrome, 10)
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.modal div.modal-footer')))
    sleep(2)
#3. Нажатие на кнопку Close
    close_button.click()
    sleep(1)

sleep(2)

#FIREFOX
with webdriver.Firefox() as firefox:
#1. Открыть страницу по ссылке
    firefox.get('http://the-internet.herokuapp.com/entry_ad')
#2. Открытие модального окна
    wait = WebDriverWait(firefox, 10)
    close_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'div.modal div.modal-footer')))
    sleep(2)
#3. Нажатие на кнопку Close
    close_button.click()
    sleep(1)

sleep(2)

#Закрытие страницы
chrome.quit()
firefox.quit()