from screenpy import Actor, given, then, when
from screenpy.actions import See
from screenpy.pacing import act, scene
from screenpy_selenium.actions import Open, SaveScreenshot, Wait
from screenpy.resolutions import (
    ContainsTheText,
    IsEqualTo,
    ContainsItemMatching,
    IsEmpty
)
from screens.login import LoginPage
from screens.home_screen import HomePage
from tasks.login_task import LogIn
from tasks.add_product_task import AddProductTask
from tasks.remove_product_task import RemoveProductTask
from questions.SearchNumberCart import SearchNumberCart
from questions.SearchLogInResult import SearchLogInResult

@act("Search")
@scene("remove product")
def test_remove_product(Dev: Actor) -> None:
    given(Dev).was_able_to(Open.their_browser_on(LoginPage().URL), LogIn.log_in(), Open.their_browser_on(HomePage.URL), AddProductTask())
    when(Dev).attempts_to(RemoveProductTask())
    then(Dev).should(
        See.the(SearchLogInResult(), ContainsTheText("Add to cart")),
        # See.the(SearchNumberCart(), ContainsItemMatching(r"^([Ss]pam ?)+")),
    )
