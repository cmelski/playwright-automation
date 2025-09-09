from playwright.sync_api import expect


class OrderDetailPage:

    def __init__(self, page):
        self.page = page

    def verify_order_detail(self, order_id):
        expect(self.page.locator('body')).to_contain_text(order_id)