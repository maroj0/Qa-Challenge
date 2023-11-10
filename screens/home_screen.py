from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from screenpy_selenium import Target


class HomePage:

    URL = 'https://www.saucedemo.com/inventory.html'
    BUTTON_ADD_TO_CART = Target.the("add to cart").located_by((By.ID,"add-to-cart-sauce-labs-backpack"))
    BUTTON_REMOVE_TO_CART = Target.the("remove to cart").located_by((By.ID,"remove-sauce-labs-backpack"))
    SELECT_FILTER = Target.the('filter button').located_by((By.XPATH,"//select[@class='product_sort_container']"))
    # VALUE_LESS = Select(SELECT_FILTER)   
    CART = Target.the('cart').located_by((By.ID,'shopping_cart_container'))
    CART_NUMBER = Target.the('products number in cart').located_by((By.XPATH,"//a[@class='shopping_cart_link']/span[@class='shopping_cart_badge']"))
    # LIST_ITEMS = Target.the("list of product").located_by((By.ID,"inventory_container"))
    LIST_ITEMS = Target.the("list of product").located_by((By.XPATH,"//div[@class='inventory_list']"))

