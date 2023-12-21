from selenium import webdriver
import pickle
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Function to save cookies
def save_cookies(driver, cookies_file):
    with open(cookies_file, 'wb') as file:
        pickle.dump(driver.get_cookies(), file)

# Chrome options
chrome_options = Options()

# Start Chrome WebDriver with the explicit path to chromedriver.exe and options
driver_path = r'C:\Users\fahis\OneDrive\Desktop\assesment\scraper\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Input link from the user
link = input("Enter the link: ")
driver.get(link)

# Manually log in or use your login automation here
# For example, you might fill in login details and submit the form

# Wait for the login process to complete
input("Login completed. Press Enter to save cookies...")

# Save cookies after logging in
save_cookies(driver, 'cookies.pkl')

# Quit the browser
driver.quit()
