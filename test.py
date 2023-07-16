from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

count = 0

while count < 10000:
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to a website and interact with it
    driver.get("https://fast-poll.com/poll/89652557")

    wait = WebDriverWait(driver, 10)
    
    try:
        accept_button = wait.until(EC.element_to_be_clickable((By.ID, "gdpr-cookie-accept")))
        accept_button.click()
    except:
        pass

    poll_items = driver.find_elements(By.CLASS_NAME, "poll-item")
    poll_items[9].click()

    footer_div = driver.find_element(By.CLASS_NAME, "poll-footer")
    button = footer_div.find_element(By.TAG_NAME, "button")
    button.click()

    # Close the driver when finished
    driver.quit()
    count += 1

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--incognito')

count = 0

while count < 10000:
    driver = webdriver.Chrome(options=chrome_options)

    # Navigate to a website and interact with it
    driver.get("https://fast-poll.com/poll/89652557")

    wait = WebDriverWait(driver, 10)

    try:
        accept_button = driver.find_element(By.ID, "gdpr-cookie-accept")
        accept_button.click()
    except:
        pass

    poll_items = driver.find_elements(By.CLASS_NAME, "poll-item")
    poll_items[9].click()

    footer_div = driver.find_element(By.CLASS_NAME, "poll-footer")
    button = footer_div.find_element(By.TAG_NAME, "button")
    button.click()

    # Close the driver when finished
    driver.quit()
    count += 1