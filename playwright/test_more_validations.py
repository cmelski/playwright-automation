import time

from playwright.sync_api import Page, expect


def test_ui_checks(page: Page):

    # #hide/display placeholder
    page.goto('https://rahulshettyacademy.com/AutomationPractice/')
    # expect(page.get_by_placeholder('Hide/Show Example')).to_be_visible()
    # page.get_by_role('button', name='Hide').click()
    # expect(page.get_by_placeholder('Hide/Show Example')).to_be_hidden()
    #
    # #alert popups
    # page.on('dialog', lambda dialog: dialog.accept())
    # page.get_by_role('button', name='Confirm').click()
    # time.sleep(5)

    # mouse hover handling

    page.locator('#mousehover').hover()
    page.get_by_role('link', name='Top').click()


    # #Frame Handling

    # page_frame = page.frame_locator('#courses-iframe')
    # page_frame.get_by_role('link', name='All Access plan').click()
    # expect(page_frame.locator('body')).to_contain_text('Happy Subscibers')

    # tables - check price of rice is equal to 37
    # page.goto('https://rahulshettyacademy.com/seleniumPractise/#/offers/')
    # col_value = None
    # for index in range(page.locator('th').count()):
    #     if page.locator('th').nth(index).filter(has_text='Price').count() > 0:
    #         col_value = index
    #         print(f'Price column index value is: {col_value}')
    #         break
    #
    # rice_row = page.locator('tr').filter(has_text='Rice')
    #rice_row_cells = [cell.text_content() for cell in rice_row.locator('td').all()]
    #print(rice_row_cells[col_value])
    #assert int(rice_row_cells[col_value]) == 37

    #or

    #expect(rice_row.locator('td').nth(col_value)).to_have_text('37')
