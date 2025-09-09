from playwright.sync_api import expect

from .orders_history import OrdersHistoryPage


class DashboardPage:

    def __init__(self, page):
        self.page = page

    def go_to_orders(self):
        self.page.locator("button[routerlink='/dashboard/myorders']").click()
        orders_history_page = OrdersHistoryPage(self.page)
        return orders_history_page

    def verify_dashboard_url(self):
        expect(self.page).to_have_url('https://rahulshettyacademy.com/client/dashboard/dash')
