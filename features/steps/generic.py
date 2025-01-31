# Step definitions for about page
from urllib.parse import urljoin
from setupSelenium import * 


@given('I\'m an sml portal user')
def auth_user(context):
    driver.get(context.config.userdata.get("host"))
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == 'An open source library for statistical code approved by the ONS'


@when('I refresh the page')
def refresh_page(context):
    driver.current_url
    driver.refresh()
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))


@when('I navigate to the "{page}" page')
def navigate_to_page(context, page):
    driver.get(urljoin(context.config.userdata.get("host") + "resources/", page))
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))


@when('I navigate to "{url}"')
def navigate_to_url(context, url):
    driver.get(urljoin(context.config.userdata.get("host"), url))
    WebDriverWait(driver, timeout=timeout).until(EC.presence_of_element_located((By.ID, 'main-content')))


@then('The title of the page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h1")).text
    assert page_title == title

@then('The title of the help centre page is "{title}"')
def check_title(context, title):
    page_title = WebDriverWait(driver, timeout=timeout).until(lambda d: d.find_element(By.TAG_NAME, "h3")).text
    assert page_title == title


@then('The subtitle of the page is "{subtitle}"')
def check_subtitle(context, subtitle):
    page_subtitle = WebDriverWait(driver, timeout=10).until(lambda d: d.find_element(By.ID, "page-subtitle")).text
    assert page_subtitle == subtitle