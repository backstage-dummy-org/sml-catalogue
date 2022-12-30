# Tests for the date adjustment link

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from behave import *
driver = webdriver.Chrome()


@given('I\'m an sml portal user trying to get to the date adjustment method')
def auth_user(context):
    driver.get('http://localhost:5000/')


@when('I navigate to the date adjustment page')
def navigate_to_date_adjustment_method(context):
    driver.find_element(By.ID, value='title1').click()
    driver.find_element(By.LINK_TEXT, value='Date adjustment').click()


@then('The title of the date adjustment page is "{title}"')
def check_title(context, title):
    page_title = driver.find_element(By.TAG_NAME, "h1").text
    assert page_title == title
