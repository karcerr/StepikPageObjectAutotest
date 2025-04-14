import time

import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage

product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"



def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, product_link)
    page.open()
    page.go_to_login_page()

