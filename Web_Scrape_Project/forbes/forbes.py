from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

# Excplicit wait
def document_initialised(driver):
    return driver.execute_script("return initialised")

url = 'https://www.makro.co.za/electronics-computers/computers-tablets/laptops-notebooks/premium/msi-gf63-thin-10uc-core-i7-3050-15-6-144hz-fhd-gaming-laptop/p/9722f7c3-2059-493b-ad59-9f9f2af8c05d?gclid=CjwKCAjwo8-SBhAlEiwAopc9WzmyKCRo0jWbmSyM4I9PeGd74zZySVuTYU3Rmm3rhOIlc6XjRsvR0BoCgEgQAvD_BwE#'
# driver.

driver = webdriver.Chrome(r'C:\chromedriver.exe')
driver.get(url)
time.sleep(10)
load_more_button = driver.find_element(By.CLASS_NAME,"load-more")
print(load_more_button)
while load_more_button.is_displayed():
    load_more_button.click()
    time.sleep(10)

# try:
#     load_more_button = WebDriverWait(driver,300).until(EC.presence_of_element_located(By.CLASS_NAME,"load-more"))
#     print('Found element')
# except:
#     print("Something went wrong")
# finally:
#     driver.quit()

