#
# Simple POC for automated testing of the iOS Calendar POC App
#
# Author:    btweed
# Date:      8/11/2016
#
import os
import unittest
import yaml

from appium import webdriver

from pages import LoginPage, TodayPage

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)


class ConfigLoader(object):

    def __init__(self):
        file = open('config.yaml')
        yaml_dict = yaml.load(file)
        self.credentials = yaml_dict['valid_user_creds']
        self.app_path = yaml_dict['app_path']

    def get_credentials(self):
        return self.credentials

    def get_app_path(self):
        return self.app_path


class AppleTasksTest(unittest.TestCase):
    """ This is the base class from which all other tests inherit """
    def setUp(self):
        super(AppleTasksTest, self).setUp()
        config_loader = ConfigLoader()
        app_path = config_loader.get_app_path()

        desired_capabilities = {'platformName': 'iOS', 'platformVersion': '9.3',
                                'deviceName': 'iPhone 6s Plus',
                                'app': PATH(app_path)}

        grid_url = 'http://localhost:4723/wd/hub'
        self.driver = webdriver.Remote(grid_url, desired_capabilities)
        self.credentials = config_loader.get_credentials()

    def tearDown(self):
        super(AppleTasksTest, self).tearDown()
        self.driver.quit()


class LoginTest(AppleTasksTest):

    def testLogin(self):
        """
        This test checks login and logout functionality.
        Steps:
        1. Login using a valid email/password combination
        2. Land on the Today page.
        3. Tap the 'X'
        5. Land back on the login page
        """
        login_page = LoginPage(self.driver)
        login_page.set_email(self.credentials['email'])
        login_page.set_password(self.credentials['password'])
        login_page.click_login_button()

        today_page = TodayPage(self.driver)
        today_page.wait_for_it()

        # Confirm login was successful
        self.assertTrue('Today' in self.driver.page_source)

        # Now sign out
        today_page.sign_out()

        # Confirm you are taken back to the login page
        login_page.wait_for_it()


if __name__ == '__main__':
    """ Just runs the one testcase (for now) """
    suite = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
    unittest.TextTestRunner(verbosity=2).run(suite)





