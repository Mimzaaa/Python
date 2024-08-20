from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager

chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
firefox = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))

#1. Открыть страницу по ссылке
chrome.get('http://the-internet.herokuapp.com/add_remove_elements/')
firefox.get('http://the-internet.herokuapp.com/add_remove_elements/')

#2. Пять раз кликните на кнопку Add Element
for _ in range(5):
    add_button = chrome.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_button.click()
    add_button = firefox.find_element(By.CSS_SELECTOR, "button[onclick='addElement()']")
    add_button.click()
    sleep(1)

#3. Соберите со страницы список кнопок Delete
chrome_delete_buttons = chrome.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")
firefox_delete_buttons = firefox.find_elements(By.CSS_SELECTOR, "button[onclick='deleteElement()']")

#4. Выведите на экран размер списка
print(f"Количество кнопок Delete на странице Chrome: {len(chrome_delete_buttons)}")
print(f"Количество кнопок Delete на странице Firefox: {len(firefox_delete_buttons)}")

#Закрытие страницы
chrome.quit()
firefox.quit()