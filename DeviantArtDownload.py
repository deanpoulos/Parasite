from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve

# Initialise browser
driver = webdriver.Chrome()
driver.get('https://deviantart.com')

# Click on the first image
first_image = driver.find_element_by_xpath(
    '/html/body/div/div[2]/div[2]/div/section/div/div/div[2]/div/div[1]/div/div[1]/div/section/a/div/img'
)
first_image.click()

# Wait for page to load
delay = 3
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/div[1]/div/div[2]/div[1]/img')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")

# Download full image
image = driver.find_element_by_xpath(
    '/html/body/div/main/div[2]/div[1]/div[1]/div/div[2]/div[1]/img'
)
src = image.get_attribute('src')
driver.get(src)
print(src)
urlretrieve(src, "C:/Users/deanp/Documents/Parasite/images/image.png")

# Close the browser
driver.quit()