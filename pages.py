from appium.webdriver.common.touch_action import TouchAction

from locators import LoginPageLocators, TodayPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Page(object):
    """ Parent class for all pages, holds the reference to webdriver instance """

    def __init__(self, webdriver_reference):
        self.driver = webdriver_reference


class LoginPage(Page):
    """ Represents the app's login page, used to manipulate login inputs """

    SHORT_WAIT = 3

    def set_email(self, email_to_set):
        assert email_to_set is not None
        email_textbox = self.driver.find_element(*LoginPageLocators.EMAIL_TEXTBOX)
        email_textbox.send_keys(email_to_set)

    def set_password(self, password_to_set):
        assert password_to_set is not None
        password_textbox = self.driver.find_element(*LoginPageLocators.PASSWORD_TEXTBOX)
        password_textbox.send_keys(password_to_set)

    def click_login_button(self):
        login_button = self.driver.find_element(*LoginPageLocators.LOGIN_BUTTON)
        TouchAction(self.driver).tap(login_button).perform()

    def wait_for_it(self):
        """ Waits for the app to be on the initial login page """
        WebDriverWait(self.driver, self.SHORT_WAIT).until(
            ec.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )


class TodayPage(Page):

    SHORT_WAIT = 5

    def sign_out(self):
        """ Click the X in the upper right hand corner of the app to go back to login screen
        """
        sign_out_button = self.driver.find_element(*TodayPageLocators.SIGN_OUT_BUTTON)
        TouchAction(self.driver).tap(sign_out_button).perform()

    def tap_this_week(self):
        pass

    def wait_for_it(self):
        """ Wait until the application is displaying the Today page """
        WebDriverWait(self.driver, self.SHORT_WAIT).until(ec.presence_of_element_located(TodayPageLocators.TODAY_BUTTON))





