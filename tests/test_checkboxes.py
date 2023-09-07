import pytest

from pages.checkboxes_page import CheckBoxesPage


@pytest.mark.skip
def test_checkboxes(page):
    page = CheckBoxesPage(page)
    page.open_the_page()
    page.click_first_checkbox()
    page.click_submit_button()
    page.check_result_is_as_data('one1')
