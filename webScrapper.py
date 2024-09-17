from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import os

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("-incognito")

# Uncomment the line corresponding to your operating system
# chromedriver_path = './chromedriver'  # For Linux systems
chromedriver_path = './chromedriver.exe'  # For Windows Systems

def create_webdriver():
    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)

# Open the website
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")