import time
import pytest

from playwright.sync_api import Page, Playwright, expect, Dialog # page fixture comes from this class


# playwright and page fixture is already included in pytest-playwright package

def test_playwright_basics(playwright):
    # chromium applies to chrome and microsoft edge
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto('https://rahulshettyacademy.com')


# chromium headless mode, 1 single context
# pass in page: Page to get the method suggestions menu
# to run in headless=False mode, right click and modify run config and under Additional arguments,
# add --headed
@pytest.mark.tcid2
def test_playwright_shortcut(page: Page):
    print('Headed mode')
    page.goto('https://rahulshettyacademy.com')



@pytest.mark.tcid1
def test_core_locators_invalid_login(page: Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('rahulshettyacademy')

    # incorrect password
    page.get_by_label('Password:').fill('wrongpassword')
    page.get_by_role('combobox').select_option('consult')
    page.get_by_role('link', name='terms and conditions').click()
    # css selector
    # -- #terms is by id; .text-info is by class; or tag name
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()

    # playwright has autowait so you don't need to write code to wait

    # assertion to check for error message when wrong password is entered
    expect(page.get_by_text('Incorrect username/password.')).to_be_visible()

    # don't need time.sleep if assertion is used
    # time.sleep(5)


@pytest.mark.tcid2
def test_core_locators_valid_login(page: Page):
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('rahulshettyacademy')

    # correct password
    #page.get_by_label('Password:').fill('learning')
    page.locator('#password').fill('learning')
    page.get_by_role('combobox').select_option('consult')
    page.get_by_role('link', name='terms and conditions').click()
    # css selector
    # -- #terms is by id; .text-info is by class; or tag name
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()


    # playwright has autowait so you don't need to write code to wait

    # assertion to check for error message when wrong password is entered
    expect(page).to_have_url('https://rahulshettyacademy.com/angularpractice/shop')

    # don't need time.sleep if assertion is used
    #time.sleep(5)


def test_firefox(playwright: Playwright):
    firefox_browser = playwright.firefox
    browser = firefox_browser.launch(headless=False)
    page = browser.new_page()
    page.goto('https://rahulshettyacademy.com')
    time.sleep(5)
