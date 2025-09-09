import json

import requests
from playwright.sync_api import Playwright

orders_payload = {
    "orders": [
        {
            "country": "Canada",
            "productOrderedId": "67a8df56c0d3e6622a297ccd"
        }
    ]
}


class APIBase:

    def get_token(self, playwright: Playwright):
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com/')
        response = api_request_context.post(url='api/ecom/auth/login',
                                            data={'userEmail': 'c_melski@yahoo.com', 'userPassword': 'bestDAY2011'})
        assert response.ok
        token = response.json()['token']
        return token

    def create_order(self, playwright: Playwright):
        token = self.get_token(playwright)
        api_request_context = playwright.request.new_context(base_url='https://rahulshettyacademy.com/')
        headers = {'Content-Type': 'application/json',
                   'Authorization': token
                   }
        response = api_request_context.post(url='api/ecom/order/create-order',
                                            data=json.dumps(orders_payload), headers=headers)
        assert response.status == 201
        order_id = response.json()['orders'][0]
        return order_id
