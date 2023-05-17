from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('launch firefox browser')
def set_impl(context):
    context.driver = webdriver.Firefox()


def login(context):
    context.driver.find_element(By.ID, "login-button").click()


def logout(context):
    context.driver.find_element(By.ID, "react-burger-menu-btn").click()
    context.driver.find_element(By.ID, "logout_sidebar_link").click()


def username(context, user_name):
    username_input = context.driver.find_element(By.ID, "user-name")
    username_input.clear()
    username_input.send_keys(user_name)


def password(context, user_password):
    password_input = context.driver.find_element(By.ID, "password")
    password_input.clear()
    password_input.send_keys(user_password)


def get_error(context):
    return context.driver.find_element(By.CLASS_NAME, "error-message-container")


@when('open saucedemo homepage')
def open_home_page(context):
    context.driver.get("https://www.saucedemo.com/")


@then('test 1 - logging without login and password')
def test_1(context):
    login(context)
    error = get_error(context).is_displayed()
    assert error is True


@then('test 2 - logging with wrong username')
def test_2(context):
    username(context, "wrong-user")
    login(context)
    error = get_error(context)
    assert error.text == "Epic sadface: Password is required"


@then('test 3 - logging with incorrect username and password')
def test_3(context):
    username(context, "wrong-user")
    password(context, "wrong-password")
    login(context)
    error = get_error(context)
    assert error.text == "Epic sadface: Username and password do not match any user " \
                         "in this service"


@then('test 4 - logging without username and incorrect password')
def test_4(context):
    username(context, "")
    password(context, "wrong_password")
    login(context)
    error = get_error(context)
    assert error.text == "Epic sadface: Username is required"


@then('test 5 - logging with correct username and without password')
def test_5(context):
    username(context, "standard_user")
    password(context, "")
    login(context)
    error = get_error(context)
    assert error.text == "Epic sadface: Password is required"


@then("test 6 - logging with correct username and wrong password")
def test_6(context):
    username(context, "standard_user")
    password(context, "wrong_password")
    login(context)
    error = get_error(context)
    assert error.text == "Epic sadface: Username and password do not match any user " \
                         "in this service"


@then("test 7 - logging with incorrect username and correct password")
def test_7(context):
    username(context, "what_user?")
    password(context, "secret_sauce")
    login(context)
    error = get_error(context)
    assert error.text == "Epic sadface: Username and password do not match any user " \
                         "in this service"


@then("test 8 - logging with correct username and correct password")
def test_8(context):
    username(context, "standard_user")
    password(context, "secret_sauce")
    login(context)
    sidebar = context.driver.find_element(By.ID, "react-burger-menu-btn").is_displayed()
    assert sidebar is True


@then("logout back to homepage")
def logout_to_homepage(context):
    logout(context)


@then('close firefox browser')
def close_browser(context):
    context.driver.quit()
