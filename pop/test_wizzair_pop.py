# -*- coding: utf-8 -*-
import unittest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from selenium import webdriver
from time import sleep

class WizzairRegistration(unittest.TestCase):
    def setUp(self):
        # Tworzę profil (opcje) uruchomienia Firefoxa
        profile = webdriver.FirefoxProfile()
        # Wyłączam lokalizację
        profile.set_preference("geo.enabled", False)
        # Uruchamiam "sprofilowanego" Firefoxa
        self.driver = webdriver.Firefox(firefox_profile = profile)
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl#/")

    def tearDown(self):
        self.driver.quit()

    def test_correct_registration(self):
        home_page = HomePage(self.driver)
        home_page.click_zaloguj_button()
        login_page = LoginPage(self.driver)
        login_page.click_rejestracja_button()
        sleep(4)

if __name__ == '__main__':
    unittest.main(verbosity=2)
