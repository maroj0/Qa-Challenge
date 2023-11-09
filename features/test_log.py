from typing import Generator

from screenpy import Actor, given, then, when
from screenpy.actions import See
from screenpy.pacing import act, scene
from screenpy_selenium.actions import Open
from screenpy.resolutions import (
    ContainsTheText,
)
from screens.login import LoginPage
from tasks.login_task import LogIn
from questions.SearchLogInResult import SearchLogInResult



@act("Search")
@scene("Navigate to log in")
def test_search_log_in(Dev: Actor) -> None:
    given(Dev).was_able_to(Open.their_browser_on(LoginPage().URL))
    when(Dev).attempts_to(LogIn.log_in())
    then(Dev).should(
        See.the(SearchLogInResult(), ContainsTheText("Add to cart")),
    )
