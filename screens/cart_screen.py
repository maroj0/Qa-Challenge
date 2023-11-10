from selenium.webdriver.common.by import By
from screenpy_selenium import Target


class CartPage:

    URL = 'https://www.saucedemo.com/cart.html'
    BUTTON_CHECKOUT=Target.the("button checkout").located_by((By.ID, 'checkout'))
    BUTTON_CONTINUE_SHOPPING=Target.the("button continue shopping").located_by((By.ID, 'continue-shopping'))
    CART_LIST=Target.the("list of products in the cart").located_by((By.XPATH, "//div[@class='cart_list']"))
    BUTTON_REMOVE=Target.the("list of products in the cart").located_by((By.ID, 'remove-sauce-labs-backpack'))
    ELEMENT=Target.the("list of products in the cart").located_by((By.ID, "//div[@class='cart_item']"))