# GitHub Follow Bot

This is a simple Python script that uses the Selenium library to automate following users on GitHub. 

## Description

A GitHub Follow Bot made using Selenium application. After receving the necessary information from the user, the bot itself runs. 
It is designed to work with the Google Chrome browser. This bot is capable of both following new people and also decreasing your own followers.

## Installation

1. Clone or download the repository.
2. Install the required Python packages using pip:
   
```   
    pip install -r requirements.txt
```

3. Download and install the latest version of the [Google Chrome browser](https://www.google.com/chrome/?brand=FNES) from the official website, incase you do not have one.
   
* Important : Although I have placed the executable Chrome Driver in the main folder. But in case this version(111.0.5563.148) becomes outdated, just download the latest driver from the [official website](https://chromedriver.chromium.org/downloads) and paste it in the same directory as the main.py script.

## Usage

1. Open the main.py file and set the USERNAME and PASSWORD variables to your GitHub username and password, respectively (needed to be done only once).
2. Further, set the USERNAME of the user whose followers you want to follow.
3. Below the username, you'll have an option to either increase your following, or decrease it. 
   Enter "0" to increase and "1" to decrease.

The script will start the Chrome browser and navigate to the GitHub website. It will log in to your account using the credentials you specified before. Finally, it will start following every person who is following the specified person i.e, their followers.

## Disclaimer

This bot is intended for educational purposes only. The use of this bot to automate following users on GitHub may violate the terms of service of the website. Use at your own risk.

## Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request. I welcome any contributions or suggestions!

## Authors
- [@arpy8](https://www.github.com/arpy8)