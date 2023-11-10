from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click
from screens.home_screen import HomePage
from screens.cart_screen import CartPage


class RemoveProductCartTask:
    

    @staticmethod
    def RemoveProductCartTask() -> "RemoveProductCartTask":
        return RemoveProductCartTask()
    
    @beat('add a product in the cart')
    def perform_as(self, the_actor:Actor) -> None:
        the_actor.attempts_to(
            Click.on(HomePage.CART),
            Click.on(CartPage.BUTTON_REMOVE),
            Wait.for_the(CartPage.ELEMENT).to_disappear(),
            Click.on(CartPage.BUTTON_CONTINUE_SHOPPING)
            )

    def __init__(self) -> None:
        pass
