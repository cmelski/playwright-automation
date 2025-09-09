import pytest
from pytest_bdd import given, when, then, parsers, scenarios
from page_objects.login import LoginPage
from utils.api_base_framework import APIBase
import time

# define the path to the feature file
scenarios('features/order_transaction.feature')

# define a fixture and update the fixture as you go with data you will need in each function
@pytest.fixture
def shared_data():
    return {}


# use parsers.parse when passing in variables in curly braces in your given/when/then
@given(parsers.parse('order is placed using a {user_email} and {password}'))
def place_order_item(playwright, user_email, password, shared_data):
    user_credentials = dict()
    user_credentials['user_email'] = user_email
    user_credentials['password'] = password

    # use api call to submit order
    api_utils = APIBase()
    order_id = api_utils.create_order(playwright, user_credentials)
    shared_data['order_id'] = order_id


@given('the user is on landing page')
def user_on_landing_page(browser_instance, shared_data):
    login_page = LoginPage(browser_instance)
    shared_data['login_page'] = login_page


@when(parsers.parse('I log into portal with {user_email} and {password}'))
def login_to_portal(user_email, password, shared_data):
    login_page = shared_data['login_page']
    dashboard_page = login_page.login(user_email, password)
    shared_data['dashboard_page'] = dashboard_page
    time.sleep(2)


@when('navigate to orders page')
def navigate_to_orders_page(shared_data):
    dashboard_page = shared_data['dashboard_page']
    order_history_page = dashboard_page.go_to_orders()
    shared_data['order_history_page'] = order_history_page


@when('select the order ID')
def select_order_id(shared_data):
    order_history_page = shared_data['order_history_page']
    order_id = shared_data['order_id']
    order_detail_page = order_history_page.select_order(order_id)
    shared_data['order_detail_page'] = order_detail_page


@then('order message is successfully displayed')
def validate_order_message(shared_data):
    order_detail_page = shared_data['order_detail_page']
    order_id = shared_data['order_id']
    order_detail_page.verify_order_detail(order_id)
