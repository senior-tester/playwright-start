import re
import pytest
from playwright.sync_api import Page, expect


def test_first(page: Page):
    page.goto('https://www.google.com/')
    expect(page).to_have_title('Google')
    mail_link = page.get_by_role('link', name='mail')
    expect(mail_link).to_have_attribute('href', 'https://mail.google.com/mail/&ogbl')
    input_field = page.locator('css=[name="q"]')
    # input_field = page.locator('xpath=//*[@name="q"]')
    input_field.fill('cat')
    search_button = page.locator('xpath=(//*[@name="btnK"])[2]')
    search_button.click()
    expect(page).to_have_title(re.compile('cat'))
    print(page.title())
