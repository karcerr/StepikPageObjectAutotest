from .base_page import BasePage
from .locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"

    def click_add_to_cart_button(self):
        button = self.browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        button.click()

    def added_name_correct(self):
        name = self.browser.find_element(By.CSS_SELECTOR, "h1:first-of-type")
        name_added = self.browser.find_element(By.CSS_SELECTOR, "#messages .alert-success:first-of-type strong")
        assert name.text == name_added.text, "Names do not match"

    def added_price_correct(self):
        price = self.browser.find_element(By.CSS_SELECTOR, "p.price_color")
        price_added = self.browser.find_element(By.CSS_SELECTOR, "#messages .alert-info strong")
        assert price.text == price_added.text, "Prices do not match"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*MainPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
    def success_message_disappeared(self):
        assert self.is_disappeared(*MainPageLocators.SUCCESS_MESSAGE), \
            "Success message has not disappeared after 4 seconds"
