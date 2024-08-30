from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/textinput")


string = driver.find_element(By.ID, 'newButtonName')
string.clear()
string.send_keys("SkyPro")

button = driver.find_element(By.ID, 'updatingButton').click()

wait = WebDriverWait(driver, 10)
updated_button = wait.until(EC.presence_of_element_located((By.ID, 'updatingButton')))
button_text = updated_button.text

print(button_text)
