from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login URL is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email, password):
        email_field= self.browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        password_field=self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        confirmation_field = self.browser.find_element(*LoginPageLocators.PASSWORD_CONFIRMATION_FIELD)
        email_field.send_keys(email)
        password_field.send_keys(password)
        confirmation_field.send_keys(password)
        registration_button=self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_BUTTON)
        registration_button.click()
