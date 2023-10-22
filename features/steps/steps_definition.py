from behave import *
from time import sleep
from selenium.webdriver.common.by import By
from helper.SeleniumHelper import SeleniumHelper

main_page = "https://www.saucedemo.com/"

# =========================== LOGIN FUNCTIONALITY ==================================

@given(u'user is on the login page')
def user_is_on_login_page(context):
    # context.driver.get('https://www.saucedemo.com/')
    SeleniumHelper().open_page(context.driver, main_page)
    assert 'Swag Labs' in context.driver.title



@when('user enters {username} and {password}')
def user_enters_credentials(context, username, password):
    username_field = context.driver.find_element(By.ID, 'user-name')
    password_field = context.driver.find_element(By.ID, 'password')
    login_button = context.driver.find_element(By.ID, 'login-button')
    username_field.send_keys(username)
    password_field.send_keys(password)
    login_button.click()
    sleep(2)

@then('user is {expected_result}')
def user_check_result(context, expected_result):
    if expected_result == 'redirected to product page':
        assert context.driver.current_url == 'https://www.saucedemo.com/inventory.html'
    elif expected_result == 'sees an error message':
        error_button = context.driver.find_element(By.CSS_SELECTOR, '.error-button')
        assert error_button.is_displayed()
        error_message = "Epic sadface: Username and password do not match any user in this service"
        assert error_message in context.driver.page_source
        sleep(4)



# =========================== PRODUCT_SORT ==================================

@given(u'user is logged in')
def user_login(context):
    SeleniumHelper().open_page(context.driver, main_page)
    username = context.driver.find_element(By.ID, 'user-name')
    password = context.driver.find_element(By.ID, 'password')
    login_button = context.driver.find_element(By.ID, 'login-button')
    username.send_keys("standard_user")
    password.send_keys("secret_sauce")
    login_button.click()
    sleep(2)

@when('user selects Name Z to A option from the product sort')
def select_z_a(context):
    sort_button = context.driver.find_element(By.CLASS_NAME, 'product_sort_container')
    sort_button.click()
    sleep(2)
    sort_name = context.driver.find_element(By.XPATH, "//option[@value='za']")
    sort_name.click()

@then('products are sorted alphabetically from Z to A')
def verify_a_z(context):
    product_names = context.driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    assert product_names[0].text == 'Test.allTheThings() T-Shirt (Red)'
    assert product_names[-1].text == 'Sauce Labs Backpack'


