import time

from playwright.sync_api import Page, expect


def test_UI_validation_dynamic_script(page: Page):
    # iphone X and Nokia Edge -- > verify 2 items are showing in cart
    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    page.get_by_label('Username:').fill('rahulshettyacademy')
    page.get_by_label('Password:').fill('learning')
    page.get_by_role('combobox').select_option('consult')
    page.locator('#terms').check()
    page.get_by_role('button', name='Sign In').click()
    # use filters when there are many of the same elements
    iphone_product = page.locator('app-card').filter(has_text='iphone X')
    iphone_price = iphone_product.locator('.card-body').locator('h5').inner_text()
    iphone_product.get_by_role('button').click()
    nokia_product = page.locator('app-card').filter(has_text='Nokia Edge')
    nokia_price = nokia_product.locator('.card-body').locator('h5').inner_text()
    nokia_product.get_by_role('button').click()

    page.get_by_text('Checkout').click()  # partial text will work
    time.sleep(5)
    # assertions
    expect(page.locator('.media-body')).to_have_count(2)
    expect(page.locator('.media-heading').filter(has_text='iphone X')).to_have_text('iphone X')
    expect(page.locator('.media-heading').filter(has_text='Nokia Edge')).to_have_text('Nokia Edge')
    prices = []
    total_price = 0
    table = page.locator('table')
    table_body = table.locator('tbody')
    table_rows = table_body.locator('tr').all()
    for row in table_rows:
        cells = row.locator('td').all()
        cell_data = [cell.inner_text() for cell in cells]
        if 'Remove' in cell_data:
            price = cell_data[-2].split('.')[1].strip()
            prices.append(price)
        if 'Total' in cell_data:
            total_price = cell_data[-1].split()[1].strip()
        print(cell_data)
    print(prices)
    print(total_price)
    assert int(prices[0]) + int(prices[1]) == int(total_price)

def test_child_window_handler(page: Page):

    page.goto('https://rahulshettyacademy.com/loginpagePractise/')
    with page.expect_popup() as new_page:
        page.locator('.blinkingText').filter(has_text='Free Access').click()
        child_page = new_page.value
        text = child_page.locator('.red').text_content().split()
        for word in text:
            if '@'in word:
                print(f'Email found: {word}')
                assert word == 'mentor@rahulshettyacademy.com'
