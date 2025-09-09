import time

from playwright.sync_api import Page, expect, Playwright

from utils.api_base import APIBase

fake_payload_response = {"data": [], "message": "No Orders"}

#method to mock the api response
def intercept_request(route):
    route.continue_(url='https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=685a6f19129e250258b35140')

#mocking; intercepting requests from API
#in this test user is trying to view order details for an order by another user; should get an unauthorized to view order message
def test_network1(page: Page):
    page.goto('https://rahulshettyacademy.com/client/')
    #mock request:
    page.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-details?id=*', intercept_request)
    page.locator('#userEmail').fill('c_melski@yahoo.com')
    page.locator('#userPassword').fill('bestDAY2011')
    page.get_by_role('button', name='Login').click()
    time.sleep(2)


    page.locator("button[routerlink='/dashboard/myorders']").click()
    time.sleep(3)

    # api request is made at this step: clicking View so the mock will be used instead

    page.get_by_role('button', name='View').first.click()
    time.sleep(2)
    message = page.locator('.blink_me').text_content()
    print(message)
    assert message == 'You are not authorize to view this order'

#bypass logging in every time by injecting the token into the browser local storage
def test_session_storage(playwright: Playwright):
    api_base = APIBase()
    token = api_base.get_token(playwright)
    # use playwright to login to site
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    #need a script to add token to local storage
    page.add_init_script(f'''localStorage.setItem("token","{token}")''')
    page.goto('https://rahulshettyacademy.com/client/')
    time.sleep(2)
    page.locator("button[routerlink='/dashboard/myorders']").click()
    time.sleep(2)
    expect(page.get_by_text('Your Orders')).to_be_visible()

