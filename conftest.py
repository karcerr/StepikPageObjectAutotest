import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption(
        "--language", action="store", default="en", help="Choose language (e.g. 'es', 'fr')"
    )


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")

    options = Options()
    options.add_argument(f"--lang={language}")

    driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()