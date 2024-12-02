import pytest
import time
from selenium import webdriver


@pytest.fixture(scope='class')
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.liverpool.com.mx/tienda/home")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    time.sleep(5)
    driver.close()