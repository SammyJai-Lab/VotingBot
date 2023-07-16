import threading
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options


# Define a function to open a new browser window
def open_window():
    chrome_options = Options()
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--disable-features=IsolateOrigins,site-per-process")
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

# Define the number of windows to open at a time
num_windows = 6

# Define the total number of windows to open
total_windows = 6

# Loop until all windows have been opened
while total_windows > 0:
    # Create a list of threads to hold each browser window
    threads = []
    
    # Create and start a new thread for each window
    for i in range(num_windows):
        thread = threading.Thread(target=open_window)
        thread.start()
        threads.append(thread)
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()
    
    # Decrement the total number of windows by the number of windows opened in this iteration
    total_windows -= num_windows