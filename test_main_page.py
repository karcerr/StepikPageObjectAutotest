import time

import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
link = "http://selenium1py.pythonanywhere.com/"
login_link = "https://selenium1py.pythonanywhere.com/ru/accounts/login/"
promo_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
normal_product_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_promo_page(browser):
    page = MainPage(browser, promo_link)
    page.open()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()


product_base_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
urls = [f"{product_base_link}/?promo=offer{no}" for no in range(0, 10)]
@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = MainPage(browser, normal_product_link)
    page.open()
    page.click_add_to_cart_button()
    page.should_not_be_success_message()
def test_guest_cant_see_success_message(browser):
    page = MainPage(browser, normal_product_link)
    page.open()
    page.should_not_be_success_message()
@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = MainPage(browser, normal_product_link)
    page.open()
    page.click_add_to_cart_button()
    page.success_message_disappeared()



@pytest.mark.parametrize('link', urls)
def test_promo_page_4_3_4(browser, link):
    page = MainPage(browser, link)
    page.open()
    page.click_add_to_cart_button()
    page.solve_quiz_and_get_code()
    time.sleep(2)
    page.added_name_correct()
    page.added_price_correct()
    time.sleep(2)


def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()

def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
def test_login_page(browser):
    page = LoginPage(browser, login_link)
    page.open()
    page.should_be_login_url()
    page.should_be_login_form()
    page.should_be_register_form()