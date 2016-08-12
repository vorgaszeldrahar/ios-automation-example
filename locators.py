#
# A locator is used to identify/address an element in the UI. This source file is the place to reference all locators
# within the application.
#
# Locators in this source are grouped according to the page of the application, but we are not prohibited from embracing
# other organizational schemes if they fit our purposes.
#

from selenium.webdriver.common.by import By


class LoginPageLocators(object):
    # TODO: Request better identifiers for locating elements
    EMAIL_TEXTBOX = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIATextField[1]')
    PASSWORD_TEXTBOX = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIASecureTextField[1]')
    LOGIN_BUTTON = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIAButton[1]')


class TodayPageLocators(object):
    SIGN_OUT_BUTTON = (By.XPATH, '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIAButton[2]')
    TODAY_BUTTON = (By.XPATH,
                    '//UIAApplication[1]/UIAWindow[1]/UIANavigationBar[1]/UIASegmentedControl[1]/UIAButton[1]')
