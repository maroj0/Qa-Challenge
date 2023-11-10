from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from screenpy_selenium import Target


class CheckoutPage:

    URL = 'https://www.saucedemo.com/checkout-step-one.html'
    CONTINUE_BUTTON=Target.the("continue button form").located_by((By.ID, 'continue'))
    CANCEL_BUTTON=Target.the("cancel button form").located_by((By.ID, 'cancel'))
    NAME_INPUT=Target.the("first name").located_by((By.ID, 'first-name'))
    LAST_NAME_INPUT=Target.the("last name").located_by((By.ID,"last-name"))
    ZIP_INPUT=Target.the("zip code").located_by((By.ID, 'postal-code'))
    CHECK = Target.the("check next screene").located_by((By.XPATH, "//div[@class='summary_info_label summary_total_label']"))
    ERROR = Target.the("show error").located_by((By.XPATH, "//div[@class='error-message-container error']"))
