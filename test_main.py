import re
import pytest
from playwright.sync_api import Page, expect


@pytest.mark.skip
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


@pytest.mark.skip
def test_dynamic_props(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    button = page.locator('#visibleAfter')
    button.click()
    page.screenshot(type='jpeg', path='/Users/eokulik/projects/playwright-start/shot.jpg')


@pytest.mark.skip
def test_iframe(page: Page):
    page.goto('https://www.qa-practice.com/elements/iframe/iframe_page')
    # print(page.frames)
    # print(page.main_frame.child_frames)
    toggler = page.frames[1].locator('css=.navbar-toggler-icon')
    toggler.click()
    page.screenshot(type='jpeg', path='/Users/eokulik/projects/playwright-start/toggler.jpg')


@pytest.mark.skip
def test_drag(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    draggable = page.locator('#rect-draggable')
    droppable = page.locator('#rect-droppable')
    page.drag_and_drop('#rect-draggable', '#rect-droppable')
    page.screenshot(type='jpeg', path='/Users/eokulik/projects/playwright-start/drag.jpg')


@pytest.mark.skip
def test_select(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    page.locator('#id_select_state').select_option('enabled')
    page.screenshot(type='jpeg', path='/Users/eokulik/projects/playwright-start/select.jpg')


def test_hover(page: Page):
    page.goto('https://magento.softwaretestingboard.com/')
    page.locator('#ui-id-4').hover()
    page.locator('#ui-id-9').hover()
    page.screenshot(type='jpeg', path='/Users/eokulik/projects/playwright-start/hover.jpg')
