import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class SecretSauceTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_scenario1(self):
        driver = self.driver
        self.load_site()
        self.assertIn("Swag Labs", driver.title)

    def test_scenario2(self):
        self.load_site()
        # Test 1 - Login without login and password
        self.assertEqual(self.login("", ""), "Epic sadface: Username is required")
        # Test 2 - Login with incorrect username and without password
        self.assertEqual(self.login("wrong_user", ""),
                         "Epic sadface: Password is required")
        # Test 3 - Login with incorrect username and incorrect password
        self.assertEqual(self.login("wrong_user", "wrong_password"),
                         "Epic sadface: Username and password do not "
                         "match any user in this service")
        # Test 4 - Login without username and incorrect password
        self.assertEqual(self.login("", "wrong_password"),
                         "Epic sadface: Username is required")
        # Test 5 - Login with correct username and without password
        self.assertEqual(self.login("standard_user", ""),
                         "Epic sadface: Password is required")
        # Test 6 - Login with correct username and wrong password
        self.assertEqual(self.login("standard_user", "wrong_password"),
                         "Epic sadface: Username and password do not "
                         "match any user in this service")
        # Test 7 - Login with incorrect username and correct password
        self.assertEqual(self.login("wrong_user", "secret_sauce"),
                         "Epic sadface: Username and password do not match "
                         "any user in this service")
        # Test 8 - Login with correct username and correct password
        self.assertEqual(self.login("standard_user", "secret_sauce"),
                         "Login was successful")

    def test_scenario3(self):
        self.load_site()
        self.login("standard_user", "secret_sauce")
        self.assertEqual(self.add_products_to_cart(), "2")

    def tearDown(self):
        self.driver.close()

    def load_site(self):
        driver = self.driver
        driver.get("https://www.saucedemo.com/")

    def login(self, username, password):
        driver = self.driver
        login_button = driver.find_element(By.ID, "login-button")
        username_input = driver.find_element(By.ID, "user-name")
        username_input.clear()
        if username:
            username_input.send_keys(username)
        password_input = driver.find_element(By.ID, "password")
        password_input.clear()
        if password:
            password_input.send_keys(password)
        login_button.click()
        if self.check_exists_by_classname("error-message-container"):
            return driver.find_element(By.CLASS_NAME, "error-message-container").text
        if self.check_exists_by_classname("shopping_cart_link"):
            return "Login was successful"

    def check_exists_by_classname(self, classname):
        driver = self.driver
        try:
            driver.find_element(By.CLASS_NAME, classname)
        except NoSuchElementException:
            return False
        return True

    def add_products_to_cart(self):
        driver = self.driver
        backpack = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack.click()
        jacket = driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        jacket.click()

        if self.check_exists_by_classname("shopping_cart_badge"):
            return driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text


if __name__ == "__main__":
    unittest.main()
