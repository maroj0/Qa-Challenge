from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import Text

from screens.login import LoginPage


class SearchText:

    @beat("{} checks the results ...")
    def answered_by(self, the_actor: Actor) -> str:
        return Text.of(self.value).answered_by(the_actor)

    def __init__(self, value) -> None:
        self.value = value