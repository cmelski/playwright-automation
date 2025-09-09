from playwright.sync_api import Playwright, expect
import time

from page_objects.login import LoginPage


def test_invalid_login(browser_instance):
    user_email = 'c_melski@yahoo3.com'
    password = 'fdddfdf'
    login_page = LoginPage(browser_instance)
    login_page.invalid_login(user_email,password)
    expect(browser_instance.locator('#toast-container')).to_contain_text('Incorrect email or password')
    time.sleep(2)
