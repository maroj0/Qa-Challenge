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
from tasks.add_product_task import AddProductTask
from questions.SearchNumberCart import SearchNumberCart
from questions.SearchLogInResult import SearchLogInResult
from tasks.add_second_product_task import AddSecondProductTask

@act("Search")
@scene("add more than 1 product")
def test_add_product(Dev: Actor) -> None:
    given(Dev).was_able_to(Open.their_browser_on(LoginPage().URL), LogIn.log_in(), Open.their_browser_on(HomePage.URL),AddProductTask())
    when(Dev).attempts_to(AddSecondProductTask())
    then(Dev).should(
        See.the(SearchNumberCart(), IsEqualTo('2')),
    )
