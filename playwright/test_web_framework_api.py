import json
import time
import pytest
from playwright.sync_api import Playwright
from page_objects.login import LoginPage
from utils.api_base_framework import APIBase

with open('data/credentials.json') as f:
    test_data = json.load(f)
    user_credentials_list = test_data['user_credentials']



@pytest.mark.parametrize('user_credentials', user_credentials_list)
def test_e2e_web_api(playwright: Playwright, browser_instance,
                     user_credentials):  # create conftest.py file and add user_credentials fixture
    user_email = user_credentials['user_email']
    password = user_credentials['password']
    # use playwright to create page context

    # use api call to submit order
    api_utils = APIBase()
    order_id = api_utils.create_order(playwright, user_credentials)

    # Login

    login_page = LoginPage(browser_instance)
    #use the default url_start parameter in conftest.py

    dashboard_page = login_page.login(user_email, password)

    time.sleep(2)

    # go to my orders

    order_history_page = dashboard_page.go_to_orders()

    time.sleep(3)

    order_detail_page = order_history_page.select_order(order_id)

    time.sleep(2)

    # validate the View page to find the order id

    order_detail_page.verify_order_detail(order_id)
