from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# List of companies and invitation note
companies = ["HP", "Apple", "samsung"]
connection_message = ("Hello! "
                      "As a final-year software engineering student actively seeking an internship for my end-of-studies project, "
                      "I look forward to connecting and possibly discussing an interview opportunity!")

chrome_service = Service('D:/software/chromedriver-win64/chromedriver.exe')

chrome_options = Options()
chrome_options.binary_location = "C:/Program Files/Google/Chrome/Application/chrome.exe"

# Specify your Chrome profile path
chrome_options.add_argument("user-data-dir=C:/Users/mehdi/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("profile-directory=Default")

driver = webdriver.Chrome(service=chrome_service, options=chrome_options)

# Start the LinkedIn session (should be logged in)
driver.get("https://www.linkedin.com")
sleep(3)

# Function to send connection requests
def send_connection_requests():
    for company in companies:
        # Search "Recruiter at <company>"
        search_query = f"Recruiter at {company}"
        driver.get("https://www.linkedin.com/search/results/people/")
        search_box = driver.find_element(By.XPATH, "//input[contains(@aria-label, 'Search')]")
        search_box.clear()
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        sleep(3)

        connect_buttons = driver.find_elements(By.XPATH, "//button/span[text()='Connect']/..")
        for button in connect_buttons:
            try:
                button.click()
                sleep(1)

                add_note_button = driver.find_element(By.XPATH, "//button[@aria-label='Add a note']")
                add_note_button.click()
                sleep(1)

                message_box = driver.find_element(By.XPATH, "//textarea[@name='message']")
                message_box.send_keys(connection_message)
                sleep(1)

                send_button = driver.find_element(By.XPATH, "//button[@aria-label='Send invitation']")
                send_button.click()
                sleep(1)
            except Exception as e:
                print(f"Error with {company}: {e}")
                continue
        sleep(2)

send_connection_requests()
driver.quit()
