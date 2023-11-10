from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import List

from screens.cart_screen import CartPage


class SearchCartList:

    @beat("{} checks the results ...")
    def answered_by(self, the_actor: Actor) -> str:
        # return Text.of(LoginPage.HOME_CHECK).answered_by(the_actor)
        return len(List.of(CartPage.ELEMENT).answered_by(the_actor))