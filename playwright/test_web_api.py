import json
import time
import requests
import pytest
from playwright.sync_api import Page, expect, Playwright

from utils.api_base import APIBase


def create_order_api():
    headers = {'Content-Type': 'application/json',
               'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2ODU1YzljMzBlNzA2OGQzOTgyMWQ3OTkiLCJ1c2VyRW1haWwiOiJjX21lbHNraUB5YWhvby5jb20iLCJ1c2VyTW9iaWxlIjo2NTkxMzc0MTQ5LCJ1c2VyUm9sZSI6ImN1c3RvbWVyIiwiaWF0IjoxNzUwNjAwMDg4LCJleHAiOjE3ODIxNTc2ODh9.neWN5_6LsgrQ-WKvuU5gJK93Afk_m6SrJ0R3Ei4dWw0'
               }

    payload = {
        "orders": [
            {
                "country": "Canada",
                "productOrderedId": "67a8df56c0d3e6622a297ccd"
            }
        ]
    }

    response = requests.post(url='https://rahulshettyacademy.com/api/ecom/order/create-order',
                             headers=headers, data=json.dumps(payload))

    return response


@pytest.mark.tcid20
def test_e2e_web_api(playwright: Playwright):
    # use playwright to login to site
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto('https://rahulshettyacademy.com/client/')
    page.locator('#userEmail').fill('c_melski@yahoo.com')
    page.locator('#userPassword').fill('bestDAY2011')
    page.get_by_role('button', name='Login').click()
    time.sleep(2)
    # assertion to check for shopping page after successful login
    expect(page).to_have_url('https://rahulshettyacademy.com/client/dashboard/dash')

    # use api call to submit order
    api_utils = APIBase()
    order_id = api_utils.create_order(playwright)
    print(order_id)

    #go to my orders

    page.locator("button[routerlink='/dashboard/myorders']").click()
    time.sleep(3)

    #validate order created via api call is present
    #find order id in the table and click on view

    row = page.locator('tr').filter(has_text=order_id)
    row.get_by_role('button', name='View').click()
    time.sleep(2)

    #validate the View page to find the order id

    expect(page.locator('body')).to_contain_text(order_id)

    #free up memory
    context.close()



