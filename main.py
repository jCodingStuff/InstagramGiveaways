import time
from random import choice, randint

import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains

# Important variables
username = ''
password = ''
instagram_url = 'https://www.instagram.com/'
# picture_url = ''  # Real
picture_url = ''  # Fake

# Read usernames
df = pd.read_csv('ids.csv')
usernames = list(df.username.to_numpy())

# Read phrases
with open('phrases.txt') as f:
    phrases = [line.rstrip('\n') for line in f]
print('\nPhrases: {}'.format(phrases))

# Initialize the driver
driver = webdriver.Chrome()

# Go to Instagram
driver.get(instagram_url)

# Accept cookies
time.sleep(randint(1, 2))
selector_button_accept = 'button.aOOlW.bIiDR'
accept_button = driver.find_element_by_css_selector(selector_button_accept)
ActionChains(driver).click(accept_button).perform()

# LOG IN
# Put username
time.sleep(randint(2, 4))
username_input = driver.find_element_by_name('username')
username_input.send_keys(username)
# Put password
time.sleep(randint(2, 4))
password_input = driver.find_element_by_name('password')
password_input.send_keys(password)
# Click
time.sleep(randint(2, 4))
selector_log_in_button = 'button.sqdOP.L3NKy.y3zKF'
log_in_button = driver.find_element_by_css_selector(selector_log_in_button)
ActionChains(driver).click(log_in_button).perform()

# Wait [5, 10] seconds and reload Instagram (sometimes the website is crap...)
time.sleep(randint(5, 10))
driver.get(instagram_url)

# Disable notifications
selector_notifications = 'button.aOOlW.HoLwm'
notifications_button = driver.find_element_by_css_selector(selector_notifications)
ActionChains(driver).click(notifications_button).perform()

# Go to desired post
driver.get(picture_url)

# Start commenting
selector_class = 'Ypffh'
# Make sure we work with even number!
last_index = len(ids) - 1 if len(ids) % 2 == 0 else len(ids) - 2
print('\nLast index: {}'.format(last_index))
print('\nWe start commenting!')
for i in range(0, last_index, 2):  # Last parameter is the step-size
    # Sleep a bit
    time.sleep(randint(60, 100))
    # Prepare comment
    comment = '@{} @{} {}'.format(ids[i], ids[i+1], choice(phrases))
    print('\n{}'.format(comment))
    # Post
    # Get the comment area
    comment_area = driver.find_element_by_class_name(selector_class)
    comment_area.click()
    # Get the comment area (again)...
    comment_area2 = driver.find_element_by_tag_name('textarea')
    comment_area2.send_keys(comment)
    print('Keys sent!');
    # selector_post_button = 'button.sqdOP.yWX7d.y3zKF'
    post_button = driver.find_element_by_xpath("//button[@type='submit']")
    ActionChains(driver).click(post_button).perform()
    print('Posted!');
    # Wait between 1 and 2 minutes
    time.sleep(randint(60, 100))

print('\nCOMPLETED')
