from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from screenpy_selenium import Target


class HomePage:

    URL = 'https://www.saucedemo.com/inventory.html'
    BUTTON_ADD_TO_CART = Target.the("add to cart").located_by((By.ID,"add-to-cart-sauce-labs-backpack"))
    BUTTON_ADD_TO_CART_SECOND = Target.the("add to cart").located_by((By.ID,"add-to-cart-sauce-labs-bike-light"))
    BUTTON_REMOVE_TO_CART = Target.the("remove to cart").located_by((By.ID,"remove-sauce-labs-backpack"))
    SELECT_FILTER = Target.the('filter button').located_by((By.XPATH,"//select[@class='product_sort_container']"))
    CART = Target.the('cart').located_by((By.ID,'shopping_cart_container'))
    CART_NUMBER = Target.the('products number in cart').located_by((By.XPATH,"//a[@class='shopping_cart_link']/span[@class='shopping_cart_badge']"))
    LIST_ITEMS = Target.the("list of product").located_by((By.XPATH,"//div[@class='inventory_list']"))
    TITLE_FIRST_PRODUCT= Target.the("Title first product").located_by((By.ID,'item_4_title_link'))
    CHECK_DETAIL= Target.the("title product detail").located_by((By.XPATH,"//div[@class='inventory_details_desc_container']//div[@class='inventory_details_name large_size']"))
    CHECK_NAME= Target.the("title product detailas").located_by((By.XPATH,"//a[@id='item_4_title_link']/div[contains(@class,'inventory_item_name'])"))

