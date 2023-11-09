from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from screenpy_selenium import Target


class HomePage:

    URL = 'https://www.saucedemo.com/inventory.html'
    BUTTON_ADD_TO_CART = Target.the("add to cart").located_by((By.ID,"add-to-cart-sauce-labs-backpack"))
    SELECT_FILTER = Target.the('filter button').located_by((By.XPATH,"//select[@class='product_sort_container']"))
    # SELECT_FILTER = Target.the('filter button').located_by((By.CLASS_NAME,"product_sort_container"))
    CART = Target.the('cart').located_by((By.ID,'shopping_cart_container'))
    CART_NUMBER = Target.the('products number in cart').located_by((By.XPATH,"//a[@class='shopping_cart_link']/span[@class='shopping_cart_badge']"))
    # CART_NUMBER = Target.the('products number in cart').located_by((By.CLASS_NAME,"shopping_cart_badge"))

