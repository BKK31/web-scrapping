from selenium import webdriver
from selenium.webdriver.chrome.service import Service  # Import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

driver_option = webdriver.ChromeOptions()
driver_option.add_argument("-incognito")
driver_option.add_argument("--headless")

# Uncomment the line corresponding to your operating system
chromedriver_path = './chromedriver'  # For Linux systems
# chromedriver_path = './chromedriver.exe'  # For Windows Systems

def create_webdriver():
    service = Service(executable_path=chromedriver_path)
    return webdriver.Chrome(service=service, options=driver_option)

# Open the website
browser = create_webdriver()
browser.get("https://github.com/collections/machine-learning")  

# Wait for the projects to load
WebDriverWait(browser, 10).until(
    EC.presence_of_all_elements_located((By.XPATH, "//h1[@class='h3 lh-condensed']"))
)

# Extract all projects
projects = browser.find_elements(By.XPATH, "//h1[@class='h3 lh-condensed']")

# Extract information for each project
project_list = {}
for proj in projects:
    proj_name = proj.text
    proj_url = proj.find_element(By.XPATH, "a").get_attribute('href')
    project_list[proj_name] = proj_url

# Close Connection
browser.quit()

# Extracting data
project_df = pd.DataFrame.from_dict(project_list, orient = 'index')

# Manipulate the table
project_df['project_name'] = project_df.index
project_df.columns = ['project_url', 'project_name']
project_df = project_df.reset_index(drop=True)

# Export project dataframe to CSV
project_df.to_csv('project_list.csv')