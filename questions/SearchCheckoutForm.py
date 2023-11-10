from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.questions import Text

from screens.checkout_screen import CheckoutPage

class SearchCheckoutForm:
    """Find the text of the search results message.

    Abilities Required:
        BrowseTheWeb

    Examples::

        the_actor.should(
            See.the(SearchResultsMessage(), ReadsExactly("1 repository result")),
        )
    """

    @beat("{} checks the results ...")
    def answered_by(self, the_actor: Actor) -> str:
        """Direct the Actor to read off the text of the results message."""
        return Text.of(CheckoutPage.CHECK).answered_by(the_actor)