from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url: str):
        self.driver = driver
        self.base_url = base_url.rstrip('/') + '/'

    def open(self, path: str = ""):
        url = self.base_url + path.lstrip('/')
        self.driver.get(url)

    def find(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def click(self, locator, timeout=10):
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
        element.click()

    def type(self, locator, text, timeout=10, clear_first=True):
        element = self.find(locator, timeout)
        if clear_first:
            element.clear()
        element.send_keys(text)

    def get_text(self, locator, timeout=10):
        element = self.find(locator, timeout)
        return element.text

    def is_visible(self, locator, timeout=10):
        try:
            self.find(locator, timeout)
            return True
        except:
            return False
