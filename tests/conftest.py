import pytest
from selene import browser
from selenium import webdriver
import os


@pytest.fixture(scope='function', autouse=True)
def browser_management():
    browser.config.base_url = 'https://www.ozon.ru/'
    driver_options = webdriver.ChromeOptions()
#    driver_options.add_argument('--headless')
    browser.config.driver_options = driver_options
    browser.config.window_height = 1920
    browser.config.window_width = 1080
    yield

    browser.quit()
