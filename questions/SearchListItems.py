from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import List

from screens.home_screen import HomePage


class SearchListItemResult:

    @beat("{} checks the results ...")
    def answered_by(self, the_actor: Actor) -> str:
        # return Text.of(LoginPage.HOME_CHECK).answered_by(the_actor)
        return List.of(HomePage.LIST_ITEMS).answered_by(the_actor)