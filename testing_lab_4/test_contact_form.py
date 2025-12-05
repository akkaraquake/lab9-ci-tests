import pytest
import os
from selenium import webdriver
from .contact_page import ContactPage
from selenium.webdriver.chrome.options import Options
from pathlib import Path

@pytest.fixture
def driver():
    options = Options()

    # В CI (GitHub Actions) обязательно headless
    if os.getenv("CI") == "true":
        options.add_argument("--headless=new")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

# Папка, где лежит contact_page.py / contact.html
HERE = Path(__file__).resolve().parent
BASE_URL = "file:///" + HERE.as_posix() + "/"

def test_contact_form_positive(driver):
    page = ContactPage(driver, base_url=BASE_URL)

    # 1. Открываем страницу
    page.open_page()

    # 2. Заполняем все поля валидными данными
    page.fill_all_fields_valid()

    # 3. Отправляем форму
    page.submit()

    # 4. Проверяем успешное сообщение
    success_msg = page.get_success_message()
    assert "Your message has been sent" in success_msg

def test_contact_form_missing_required_name(driver):
    page = ContactPage(driver, base_url=BASE_URL)
    page.open_page()

    # Заполняем остальные поля, НО НЕ имя
    page.fill_email("john.doe@example.com")
    page.fill_phone("+1234567890")
    page.fill_message("Hello, this is a test message.")
    page.set_terms(True)

    # Пытаемся отправить форму
    page.submit()

    # Проверяем текст ошибки под полем имени
    error_msg = page.get_error_for_field("full_name")
    assert "Full Name is required" in error_msg

    # Дополнительно: не должно быть успеха
    assert not page.is_visible(page.SUCCESS_ALERT, timeout=3)
