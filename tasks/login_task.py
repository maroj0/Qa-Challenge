from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait
from screens.login import LoginPage


class LogIn:
    

    @staticmethod
    def log_in() -> "LogIn":
        return LogIn()
    
    @beat('login')
    def perform_as(self, the_actor:Actor) -> None:
        the_actor.attempts_to(
            Enter.the_text("standard_user").into(LoginPage.USERNAME_INPUT),
            Enter.the_password("secret_sauce").into(LoginPage.PASS_INPUT).then_hit(Keys.RETURN),
            Wait.for_the(LoginPage.HOME_CHECK))
