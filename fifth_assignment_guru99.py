import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from conftest import parameters
from selenium.common.exceptions import TimeoutException

link = "http://www.demo.guru99.com/V4/"

@pytest.mark.parametrize("login, password, are_credentials_valid", parameters)
def test_log_into_account(browser, login, password, are_credentials_valid):
    browser.get(link)
    input1 = browser.find_element_by_name("uid")
    input1.send_keys(login)
    input2 = browser.find_element_by_name("password")
    input2.send_keys(password)
    button = browser.find_element_by_name("btnLogin")
    button.click()
    time.sleep(5)
    try:
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        assert not are_credentials_valid, "Was unable to login with valid credentials!"
    except TimeoutException:
        login_completed=browser.find_element_by_css_selector("tr.heading3")
        assert are_credentials_valid, "Was able to login with invalid credentials2"
        assert login_completed.text==f'Manger Id : {login}', \
        "no access to the web-site"
        browser.save_screenshot("login_successful.png")
