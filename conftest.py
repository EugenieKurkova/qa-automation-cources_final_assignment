import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

login="mngr224739"
password="tUsEdem"

@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()

#login password and parameters for guru99 project
@pytest.fixture()
def valid_login():
    return login


@pytest.fixture()
def valid_password():
    return password


parameters=[
    ("mngr224739", "tUsEdem", True),
    ("mngr224738", "tUsEdem", False),
    ("mngr224739", "tUsEde", False),
    ("mngr224738", "tUsEde", False),
]


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language")

@pytest.fixture(scope="function")
def parametrized_browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    if browser_name == "chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox(firefox_profile=fp)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
