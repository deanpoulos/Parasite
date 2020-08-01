from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

# Initialise browser
driver = webdriver.Chrome()
driver.get('https://wikipedia.com')

# Change language to Latina
search_language = driver.find_element_by_id('searchLanguage')
print(search_language.text)
Select(search_language).select_by_visible_text('Latina')

# Input a textual search query
search_textinput = driver.find_element_by_id('searchInput')
search_textinput.send_keys('Marcus Aurelius')

# Make a search using the search button
search_button = driver.find_element_by_xpath(
'/html/body/div[3]/form/fieldset/button'
)
search_button.click()

# Verify that it worked
print("Current URL: " + driver.current_url)

# Save some text from the page
paragraphs = content.find_elements_by_tag_name('p')
intro_paragraph_text = paragraphs[4].text

# Close the browser
driver.quit()