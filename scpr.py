from selenium import webdriver
import pickle
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def load_cookies(driver, cookies_file):
    with open(cookies_file, 'rb') as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)
# Function to perform the automation
def automate_process():
    # Input link from the user
    link = input("Enter the link: ")

    # Chrome options
    chrome_options = Options()

    # Start Chrome WebDriver with the explicit path to chromedriver.exe and options
    driver_path = r'C:\Users\fahis\OneDrive\Desktop\assesment\scraper\chromedriver.exe'
    service = Service(driver_path)
    driver = webdriver.Chrome(service=service, options=chrome_options)
    # load_cookies(driver, 'C:/Users/fahis/OneDrive/Desktop/assesment/scraper/cookies.pkl')

    try:
        # Open the provided link
        driver.get(link)

        # Wait for the element to be present
        wait = WebDriverWait(driver, 5)
        h1_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h1.m-0')))
        # p_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'p.PageProjectViewLogout-detail-projectId')))
        # bid_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input#form-signup-bottom-bid')))
        # Get text from the elements
        h1_text = h1_element.text
        # bid = bid_input.get_attribute("placeholder")
        # p_text = p_element.text
        # bid_placeholder 

        # Write the extracted data to a text file
        with open('extracted_data.txt', 'w') as file:
            file.write(f'Content of h1 element: {h1_text}\n')
            # file.write(f'Content of p element: {p_text}\n')
            # file.write(f'Content of bid element: {bid}\n')

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the browser window
        driver.quit()

# Call the function to start the process
automate_process()
