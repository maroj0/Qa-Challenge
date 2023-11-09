from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click
from screens.home_screen import HomePage


class RemoveProductTask:
    

    @staticmethod
    def RemoveProductTask() -> "RemoveProductTask":
        return RemoveProductTask()
    
    @beat('add a product in the cart')
    def perform_as(self, the_actor:Actor) -> None:
        the_actor.attempts_to(
            Click.on(HomePage.BUTTON_REMOVE_TO_CART),
            # Wait.to_disappear(HomePage.CART_NUMBER)
            # Wait.for(HomePage.CART_NUMBER).to_disappear()
            # Wait.for_the(HomePage.CART_NUMBER).to_disappear()
            )

    def __init__(self) -> None:
        pass
