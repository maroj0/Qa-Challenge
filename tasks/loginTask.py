
class LoginTask():
    
     def login(self, user, password):
        username_input = self.browser.find_element(*self.USERNAME_INPUT)
        username_input.send_keys(user)

        password_input = self.browser.find_element(*self.PASS_INPUT)
        # password_input.send_keys(password + Keys.RETURN)
        password_input.send_keys(password)

        login_button = self.browser.find_element(*self.LOGIN_BUTTON)
        login_button.click()