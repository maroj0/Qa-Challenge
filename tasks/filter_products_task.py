from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click, Pause,Select
from screens.home_screen import HomePage
# from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


class FilterProductTask:
    

    @staticmethod
    def FilterProductTask() -> "FilterProductTask":
        return FilterProductTask()
    
    @beat('Filter products')
    def perform_as(self, the_actor:Actor) -> None:
        the_actor.attempts_to(
            Select.the_option_with_value("za").from_the(HomePage.SELECT_FILTER),
            Wait.for_the(HomePage.LIST_ITEMS),
            )



    def __init__(self,) -> None:
        pass
