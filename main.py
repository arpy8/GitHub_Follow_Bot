import os
import json
from bot import Bot
from app import main_app, perm_val_set

switch_on = False
my_list = ["", "null", None]

# reading file path of chrome driver
try:
    with open('data') as file:
        data = json.load(file)

except FileNotFoundError:
    perm_val_set()
    with open('data') as file:
        data = json.load(file)

finally:
    CHROME_DRIVER_PATH = "chromedriver.exe"
    USERNAME = data["username"]
    PASSWORD = data["password"]

# detecting null values in data.py
if USERNAME in my_list or USERNAME in my_list:
    print("Null values detected in data.txt!")
    perm_val_set()
    with open('data') as file:
        data = json.load(file)
    switch_on = True
else:
    switch_on = True

# fetching base username from user
try:
    values = main_app()
    BASE_ACCOUNT = values[1][0]
    FOLLOW_UNFOLLOW = int(values[1][1])

    github_bot = Bot(CHROME_DRIVER_PATH)
    github_bot.login(USERNAME, PASSWORD)
    switch_on = True

except ValueError or TypeError:
    switch_on = False
    exit()

# final part
finally:
    if switch_on:
        if FOLLOW_UNFOLLOW == 0:
            github_bot.follow(BASE_ACCOUNT, 0.1)

        elif FOLLOW_UNFOLLOW == 1:
            github_bot.unfollow(USERNAME, 0)

        else:
            print("Invalid input.")



