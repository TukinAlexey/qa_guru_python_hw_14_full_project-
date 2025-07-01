import pytest
from selene import browser

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def browser_screen_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()

@pytest.fixture
def open_browser_chrome(browser_screen_size):
    browser_screen_size.open('https://www.rnd-soft.ru/')



#Pfgecr через селенойд

@pytest.fixture(scope='function')
def setup_browser(request):
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    # login = os.getenv('LOGIN')
    # password = os.getenv('PASSWORD')
    # browser_url = os.getenv('BROWSER_URL')

    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser

    # attach.add_screenshot(browser)
    # attach.add_logs(browser)
    # attach.add_html(browser)
    # attach.add_video(browser)

    browser.quit()