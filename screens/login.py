from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from screenpy_selenium import Target


class LoginPage:

    URL = 'https://www.saucedemo.com/'
    USERNAME_INPUT = Target.the("userName").located_by((By.ID, 'user-name'))
    PASS_INPUT = Target.the("Pass").located_by((By.ID, 'password'))
    LOGIN_BUTTON = Target.the("Button").located_by((By.ID, "login-button"))
    HOME_CHECK = Target.the("homeCheck").located_by((By.ID, "inventory_container"))