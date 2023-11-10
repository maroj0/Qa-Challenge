from screenpy import Actor, given, then, when
from screenpy.actions import See
from screenpy.pacing import act, scene
from screenpy_selenium.actions import Open
from screenpy.resolutions import (
    ContainsTheText,
    IsEqualTo
)
from screens.login import LoginPage
from screens.home_screen import HomePage
from tasks.login_task import LogIn
from screens.checkout_screen import CheckoutPage
from tasks.incomplete_checkout_form_task import InCompleteCheckoutForm
from questions.SearchText import SearchText

@act("Buy")
@scene("Complete first form")
def test_add_product(Dev: Actor) -> None:
    given(Dev).was_able_to(Open.their_browser_on(LoginPage().URL), LogIn.log_in(), Open.their_browser_on(HomePage.URL))
    when(Dev).attempts_to(InCompleteCheckoutForm())
    then(Dev).should(
        See.the(SearchText(CheckoutPage.ERROR), ContainsTheText("Error")),
    )
