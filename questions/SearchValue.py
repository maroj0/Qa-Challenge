from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import Element

from screens.login import LoginPage


class SearchValue:

    @beat("{} checks the results ...")
    def answered_by(self, the_actor: Actor) -> str:
        return Element(self.value).answered_by(the_actor)

    def __init__(self, value) -> None:
        self.value = value