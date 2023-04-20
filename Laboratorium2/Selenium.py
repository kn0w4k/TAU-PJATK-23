import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

logger = logging.getLogger('simple_example')
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

driver = webdriver.Firefox()
logger.info("Loading saucedemo.com website")
driver.get("https://www.saucedemo.com/")

# Test 1
logger.info("Test 1 - Logging without login and password")
loginButton = driver.find_element(By.ID, "login-button")
loginButton.click()
errorMessage = driver.find_element(By.CLASS_NAME, "error-message-container")
logger.info("Error message is: " + errorMessage.text)
# Test 2
logger.info("Test 2 - Logging with incorrect username and without password")
usernameInput = driver.find_element(By.ID, "user-name")
usernameInput.clear()
usernameInput.send_keys("wrong_user")
loginButton.click()
logger.info("Error message is: " + errorMessage.text)
# Test 3
logger.info("Test 3 - Logging with incorrect username and incorrect password")
usernameInput.clear()
usernameInput.send_keys("wrong_user1")
passwordInput = driver.find_element(By.ID, "password")
passwordInput.clear()
passwordInput.send_keys("wrong_password")
loginButton.click()
logger.info("Error message is: " + errorMessage.text)
# Test 4
logger.info("Test 4 - Logging without username and incorrect password")
usernameInput.clear()
passwordInput.clear()
passwordInput.send_keys("some_sauce")
loginButton.click()
logger.info("Error message is: " + errorMessage.text)
# Test 5
logger.info("Test 5 - Logging with correct username and without password")
usernameInput.clear()
usernameInput.send_keys("standard_user")
passwordInput.clear()
loginButton.click()
logger.info("Error message is: " + errorMessage.text)
# Test 6
logger.info("Test 6 - Logging with correct username and wrong password")
usernameInput.clear()
usernameInput.send_keys("standard_user")
passwordInput.clear()
passwordInput.send_keys("wrong_password")
loginButton.click()
logger.info("Error message is: " + errorMessage.text)
# Test 7
logger.info("Test 7 - Logging with incorrect username and correct password")
usernameInput.clear()
usernameInput.send_keys("wrong_user2")
passwordInput.clear()
passwordInput.send_keys("secret_sauce")
logger.info("Error message is: " + errorMessage.text)
# Test 8
logger.info("Test 8 - Logging with correct username and correct password")
usernameInput.clear()
usernameInput.send_keys("standard_user")
passwordInput.clear()
passwordInput.send_keys("secret_sauce")
loginButton.click()
time.sleep(2)
sidebarButton = driver.find_element(By.ID, "react-burger-menu-btn")
sidebarButton.click()
logoutButton = driver.find_element(By.ID, "logout_sidebar_link")
logoutButton.click()
logger.info("User successfully logged in and out")

driver.close()
