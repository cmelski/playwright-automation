import json
import time

import pytest
from playwright.sync_api import Page
from page_objects.login import LoginPage

with open('data/no_orders.json') as f:
    no_orders_json = json.load(f)
    no_orders = no_orders_json['no_orders']

with open('data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']


# method to mock the api response
def intercept_response(route):
    route.fulfill(
        json=no_orders
    )


# mocking; intercepting responses from API and using different data in this test user has orders but we want to
# simulate a scenario where user has no orders and they see the right message on the orders page
@pytest.mark.smoke
def test_network1(browser_instance):
    user_email = user_credentials_list[0]['user_email']
    password = user_credentials_list[0]['password']
    login_page = LoginPage(browser_instance)
    #login_page.navigate()
    dashboard_page = login_page.login(user_email, password)
    # api request response to intercept: page.route method
    browser_instance.route('https://rahulshettyacademy.com/api/ecom/order/get-orders-for-customer/*', intercept_response)
    time.sleep(2)

    # api request is made at this step:
    orders_history_page = dashboard_page.go_to_orders()

    time.sleep(3)

    orders_history_page.verify_no_orders()
