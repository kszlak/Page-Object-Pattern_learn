# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class HomePageLocators():
    """ Lokatory Strony Głównej """
    ZALOGUJ_BTN = (By.XPATH, '//button[@data-test="navigation-menu-signin"]')

class LoginPageLocators():
    """ Lokatory Strony Logowania """
    REJESTRACJA_BTN = (By.XPATH, '//button[text()="Rejestracja"]')

class RegistrationPageLocators():
    """ Lokatory Strony Rejestracji """
    pass
