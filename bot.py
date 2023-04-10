import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException, \
    StaleElementReferenceException, ElementClickInterceptedException, NoSuchWindowException


class Bot:
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

    # follow
    def follow(self, base_account, time_=0.5):
        i = 0
        while True:
            i += 1
            self.driver.get(url=f"https://github.com/{base_account}?page={i}&tab=following")
            j = 0
            while j < 51:
                j += 1
                exception = 0

                try:
                    self.driver.find_element(By.XPATH, f'//*[@id="user-profile-frame"]/div/div[{j}]/div[3]/span/form['
                                                       f'1]/input[2]').click()
                except ElementNotInteractableException:
                    print("Already following the user.")
                except NoSuchElementException:
                    exception += 1
                except StaleElementReferenceException:
                    print("Stale element reference.")
                except ElementClickInterceptedException:
                    print("Element click intercepted.")

                time.sleep(time_)

                if exception > 20:
                    print("cloning completed.")
                    exit()

    # unfollow
    def unfollow(self, username, time_=0.5):
        i = 0
        while True:
            i += 1

            self.driver.get(url=f"https://github.com/{username}?page={i}&tab=following")

            j = 0
            exception = 0

            while j < 51:
                j += 1
                try:
                    self.driver.find_element(By.XPATH, f'//*[@id="user-profile-frame"]/div/div[{j}]/div[3]/span/form['
                                                       f'2]/input[2]').click()

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

                time.sleep(time_)

                if exception > 20:
                    print("process ended.")
                    exit()
