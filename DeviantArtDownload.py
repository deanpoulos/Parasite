import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
from selenium.webdriver.chrome.options import Options  

chrome_options = Options()  
chrome_options.add_argument("--headless")  

driver = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"),   chrome_options=chrome_options)  
print("Initialising Driver... ", end='')
driver.get('https://deviantart.com')
print("Initialised!")

# Click on the first image
print("Clicking on first recommended image... ", end='')
first_image = driver.find_element_by_xpath(
    '/html/body/div/div[2]/div[2]/div/section/div/div/div[2]/div/div[1]/div/div[1]/div/section/a/div/img'
)
first_image.click()
print("Clicked!") 
# Wait for page to load
print("Waiting for page to load... ", end='')
delay = 3
try:
    myElem = WebDriverWait(driver, delay).until(
        EC.presence_of_element_located((By.XPATH, '/html/body/div/main/div[2]/div[1]/div[1]/div/div[2]/div[1]/img')))
    print("Page is ready!")
except TimeoutException:
    print("Loading took too much time!")
    exit

# Fetch full image
print("Fetching full image... ", end='')
image = driver.find_element_by_xpath(
    '/html/body/div/main/div[2]/div[1]/div[1]/div/div[2]/div[1]/img'
)
print("Fetched!")

# Download full image
filename = "image"
src = image.get_attribute('src')
driver.get(src)
print("Downloading image... ", end='')
urlretrieve(src, "C:/Users/deanp/Documents/Parasite/images/" + filename + ".png")
print("Downloaded as " + filename + ".png!")

# Close the browser
driver.quit()