# _*_ coding: utf-8 -*-
import unittest
from selenium import webdriver

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        profile = self.driver = webdriver.FirefoxProfile()
        profile.set_preferences("geo.enabled", False)
        self.driver = webdriver.Firefox()
        self.driver.maximize.window()
        self.driver.get("https://wizzair.com/pl-pl")

    def tearDown(self):
        pass

    def test_correct_registration(self):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)
