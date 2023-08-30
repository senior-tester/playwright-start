from playwright.sync_api import Page


class BasePage:
    base_url = 'https://www.qa-practice.com'
    page_url = None

    def __init__(self, page: Page):
        self.page = page

    def open_the_page(self):
        if self.page_url:
            self.page.goto(f'{self.base_url}{self.page_url}')
        else:
            raise NotImplementedError('Base page can not be opened')

