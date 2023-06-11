import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture
def driver():
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    driver = webdriver.Firefox(executable_path=r'C:\WebDriver\bin\geckodriver-v0.33.0-win32\geckodriver.exe',
                               options=options)
    yield driver
    driver.quit()
