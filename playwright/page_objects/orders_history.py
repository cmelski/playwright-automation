from playwright.sync_api import expect

from .order_detail import OrderDetailPage


class OrdersHistoryPage:

    def __init__(self, page):
        self.page = page

    def select_order(self, order_id):
        row = self.page.locator('tr').filter(has_text=order_id)
        row.get_by_role('button', name='View').click()
        order_detail_page = OrderDetailPage(self.page)
        return order_detail_page

    def verify_no_orders(self):
        expect(self.page.locator('body')).to_contain_text('You have No Orders to show at this time')
