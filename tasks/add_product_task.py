from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click
from screens.home_screen import HomePage


class AddProductTask:
    

    @staticmethod
    def AddProductTask() -> "AddProductTask":
        return AddProductTask()
    
    @beat('add a product in the cart')
    def perform_as(self, the_actor:Actor) -> None:
        the_actor.attempts_to(
            Click.on(HomePage.BUTTON_ADD_TO_CART),
            # Enter.the_password("secret_sauce").into(LoginPage.PASS_INPUT).then_hit(Keys.RETURN),
            Wait.for_the(HomePage.CART_NUMBER)
            )

    def __init__(self) -> None:
        pass
