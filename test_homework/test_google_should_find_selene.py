import pytest
from selene import browser
from selene import be, have

@pytest.fixture()
def browser_open():
    browser.config.window_width = 1600
    browser.config.window_height = 800
    browser.open('https://google.com')


def test_search(browser_open):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_search_nothing(browser_open):
    browser.element('[name="q"]').should(be.blank).type('gvjdjdhdjdk').press_enter()
    browser.element('[id="topstuff"]').should(have.text('По запросу gvjdjdhdjdk ничего не найдено.'))