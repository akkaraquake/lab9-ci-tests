from selenium.webdriver.common.by import By
from .base_page import BasePage

class ContactPage(BasePage):
    PATH = "contact.html"

    # Локаторы
    FULL_NAME = (By.ID, "full_name")
    EMAIL = (By.ID, "email")
    PHONE = (By.ID, "phone")
    MESSAGE = (By.ID, "message")
    TERMS_CHECKBOX = (By.ID, "terms")
    SUBMIT_BUTTON = (By.ID, "submit")

    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert-success")
    # Пример: ошибка под конкретным полем (по data-for или id)
    ERROR_UNDER_FIELD = lambda self, field_id: (
        By.CSS_SELECTOR,
        f"[data-error-for='{field_id}']"
    )

    def open_page(self):
        self.open(self.PATH)

    def fill_full_name(self, value: str):
        self.type(self.FULL_NAME, value)

    def fill_email(self, value: str):
        self.type(self.EMAIL, value)

    def fill_phone(self, value: str):
        self.type(self.PHONE, value)

    def fill_message(self, value: str):
        self.type(self.MESSAGE, value)

    def set_terms(self, value: bool = True):
        checkbox = self.find(self.TERMS_CHECKBOX)
        is_checked = checkbox.is_selected()
        if value and not is_checked:
            checkbox.click()
        elif not value and is_checked:
            checkbox.click()

    def submit(self):
        self.click(self.SUBMIT_BUTTON)

    def get_success_message(self) -> str:
        return self.get_text(self.SUCCESS_ALERT)

    def get_error_for_field(self, field_id: str) -> str:
        locator = self.ERROR_UNDER_FIELD(field_id)
        return self.get_text(locator)

    def fill_all_fields_valid(self):
        self.fill_full_name("John Doe")
        self.fill_email("john.doe@example.com")
        self.fill_phone("+1234567890")
        self.fill_message("Hello, this is a test message.")
        self.set_terms(True)
