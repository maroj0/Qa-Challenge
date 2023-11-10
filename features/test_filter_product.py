from screenpy import Actor, given, then, when
from screenpy.actions import See
from screenpy.pacing import act, scene
from screenpy_selenium.actions import Open, SaveScreenshot, Wait
from screenpy.resolutions import (
    ContainsTheText,
    IsEqualTo,
    IsEmpty,
    IsNot,
)
from screens.login import LoginPage
from screens.home_screen import HomePage
from tasks.login_task import LogIn
from tasks.add_product_task import AddProductTask
from tasks.filter_products_task import FilterProductTask
from questions.SearchLogInResult import SearchLogInResult
from questions.SearchListItems import SearchListItemResult

@act("Search")
@scene("filter products")
def test_remove_product(Dev: Actor, browser) -> None:
    given(Dev).was_able_to(Open.their_browser_on(LoginPage().URL), LogIn.log_in(), Open.their_browser_on(HomePage.URL))
    initial_list = SearchListItemResult()
    when(Dev).attempts_to(FilterProductTask())
    then(Dev).should(
        See.the(SearchLogInResult(), ContainsTheText("Add to cart")),
        See.the(SearchListItemResult(), IsNot(IsEqualTo(initial_list))),
    )
