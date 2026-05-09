import pytest
from selenium import webdriver
from Utils.LoginPage import login

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito") # Se abre como incognito para evitar el cache

    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture
def login_in_driver(driver):
    login(driver)
    return driver