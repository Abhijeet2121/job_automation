from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.page_load_strategy = "none"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()),options=options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3598569081&distance=25&f_E=1%2C2%2C3&f_JT=F%2CI&f_WT=1%2C2%2C3&geoId=102713980&keywords=python%20developer")
driver.implicitly_wait(0.5)
time.sleep(3)

sign_in = driver.find_element(By.LINK_TEXT, "Sign in")
# sign_in = driver.find_element(By.CLASS_NAME, "btn-secondary-emphasis")
sign_in.click()
time.sleep(2)

username = driver.find_element(By.CSS_SELECTOR, "form div #username")
password = driver.find_element(By.CSS_SELECTOR, "form div #password")
username.send_keys("kabhi30@gmail.com")
password.send_keys("Abhi@9881")
button = driver.find_element(By.CSS_SELECTOR, ".login__form button")
button.click()
time.sleep(10)

job_list = driver.find_elements(By.CSS_SELECTOR, ".job-card-container--clickable")
for list in job_list:
    print("called")
    list.click()
    time.sleep(2)

    try:
        easy_apply =driver.find_element(By.CSS_SELECTOR, '.jobs-s-apply')
        # print(easy_apply.tag_name)
        easy_apply.click()
        time.sleep(2)

        phone = driver.find_element(By.CSS_SELECTOR, "input .artdeco-text-input--input")
        if phone == "":
            phone.send_keys("9881898026")

        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        # print(submit_button.tag_name)

        # if submit button is next buttton
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_modal = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
            close_modal.click()
            time.sleep(2)
            discard_button = driver.find_element(By.CLASS_NAME, "artdeco-modal__confirm-dialog-btn[1]")
            discard_button.click()
            print(" Application skipped")
            continue
        else:
            submit_button.click()
        # once submitted close the pop up window
        time.sleep(2)
        close_modal = driver.find_element(By.CLASS_NAME, "artdeco-modal__dismiss")
    
    except:
        print("No application button found, skipped")
        continue

time.sleep(2)

    