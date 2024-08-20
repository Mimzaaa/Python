from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

def blue_button_click():
#1. Открыть страницу по ссылке
    chrome.get('http://uitestingplayground.com/classattr')
    firefox.get('http://uitestingplayground.com/classattr')
#2. Кликните на синюю кнопку
    add_button = chrome.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    add_button.click()
    add_button = firefox.find_element("xpath", "//button[contains(concat(' ', normalize-space(@class), ' '), ' btn-primary ')]")
    add_button.click()
    sleep(1)

#3. Запустите скрипт три раза подряд. Убедитесь, что он отработает одинаково
for i in range(3):
    print(f"Запуск теста в Chrome {i + 1}")
    print(f"Запуск теста в Firefox {i + 1}")
    blue_button_click()
#Нажатие на ОК в модальном окне    
    chrome.switch_to.alert.accept()
    firefox.switch_to.alert.accept()

#Закрытие страницы
chrome.quit()
firefox.quit()