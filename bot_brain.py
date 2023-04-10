import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, ElementClickInterceptedException, NoSuchWindowException


class Brain:
    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    # logging in
    def login(self, USERNAME, PASSWORD):
        self.driver.maximize_window()
        self.driver.get(url="https://github.com/login")

        username = self.driver.find_element(By.NAME, "login")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        password.send_keys(Keys.ENTER)
        time.sleep(1)

    # engine
    def bot_engine(self, time_, code, base_account, username):
        i = 0
        while True:
            i += 1

            if code == 0:
                url_1 = f"https://github.com/{base_account}?page={i}&tab=following"

            elif code == 1:
                url_1 = f"https://github.com/{username}?page={i}&tab=following"

            self.driver.get(url=url_1)

            j = 0
            exception = 0

            while j < 51:
                if code == 0:
                    xpath_2 = f'//*[@id="user-profile-frame"]/div/div[{j}]/div[3]/span/form[1]/input[2]'

                elif code == 1:
                    xpath_2 = f'//*[@id="user-profile-frame"]/div/div[{j}]/div[3]/span/form[2]/input[2]'

                j += 1
                try:
                    self.driver.find_element(By.XPATH, xpath_2).click()

                except ElementNotInteractableException:
                    print("Already following the user.")

                except NoSuchElementException:
                    exception += 1

                except StaleElementReferenceException:
                    print("Stale element reference.")

                except ElementClickInterceptedException:
                    print("Element click intercepted.")

                except NoSuchWindowException:
                    print("Target window closed")
                    exit()

                time.sleep(time_)

                if exception > 20:
                    print("process ended.")
                    exit()
