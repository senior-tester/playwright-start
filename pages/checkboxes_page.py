from pages.base_page import BasePage
from playwright.sync_api import expect


first_checkbox = 'css=#id_checkboxes_0'
submit_button = 'css=#submit-id-submit'
result_text = 'css=#result-text'


class CheckBoxesPage(BasePage):
    page_url = '/elements/checkbox/mult_checkbox'

    def __init__(self, page):
        super().__init__(page)

    def click_first_checkbox(self):
        self.page.locator(first_checkbox).click()

    def click_submit_button(self):
        self.page.locator(submit_button).click()

    def check_result_is_as_data(self, data):
        result = self.page.locator(result_text)
        # assert result.inner_text() == data
        expect(result).to_have_text(data, timeout=500)

