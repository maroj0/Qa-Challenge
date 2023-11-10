from selenium.webdriver.common.keys import Keys

from screenpy import Actor
from screenpy.pacing import beat
from screenpy_selenium.actions import Enter, Wait, Click
from screens.login import LoginPage
from screens.checkout_screen import CheckoutPage
from screens.cart_screen import CartPage
from screens.home_screen import HomePage

class CompleteCheckoutForm:
    

    @staticmethod
    def CompleteCheckoutForm() -> "CompleteCheckoutForm":
        return CompleteCheckoutForm()
    
    @beat('CompleteCheckoutForm')
    def perform_as(self, the_actor:Actor) -> None:
        the_actor.attempts_to(
            Click.on(HomePage.CART),
            Wait.for_the(CartPage.BUTTON_CHECKOUT),
            Click.on(CartPage.BUTTON_CHECKOUT),
            Wait.for_the(CheckoutPage.ZIP_INPUT),
            Enter.the_text("Dev").into(CheckoutPage.NAME_INPUT),
            Enter.the_text("Dev").into(CheckoutPage.LAST_NAME_INPUT),
            Enter.the_text("1234").into(CheckoutPage.ZIP_INPUT),
            Click.on(CheckoutPage.CONTINUE_BUTTON),
            Wait.for_the(CheckoutPage.CHECK))
