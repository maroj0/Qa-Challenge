from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click
from screens.home_screen import HomePage


class OpenProductDetailTask:
    

    @staticmethod
    def OpenProductDetailTask() -> "OpenProductDetailTask":
        return OpenProductDetailTask()
    
    @beat('add a product in the cart')
    def perform_as(self, the_actor:Actor) -> None:
        the_actor.attempts_to(
            Click.on(HomePage.TITLE_FIRST_PRODUCT),
            Wait.for_the(HomePage.CHECK_DETAIL)
            )

    def __init__(self) -> None:
        pass
