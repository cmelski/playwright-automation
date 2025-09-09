from .dashboard import DashboardPage


class LoginPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto('https://rahulshettyacademy.com/client/')

    def login(self, user_email, password):
        self.page.locator('#userEmail').fill(user_email)
        self.page.locator('#userPassword').fill(password)
        self.page.get_by_role('button', name='Login').click()

        dashboard_page = DashboardPage(self.page)
        return dashboard_page

    def invalid_login(self, user_email, password):
        self.page.locator('#userEmail').fill(user_email)
        self.page.locator('#userPassword').fill(password)
        self.page.get_by_role('button', name='Login').click()