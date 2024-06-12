from selene import browser, by, have


class CartNotLogged:
    def open_main_page(self):
        browser.open('/')
        browser.open('/')

    def check_items_quantity_in_cart(self):
        browser.element(by.css('a[href*="cart"]')).should(have.exact_text('0'))

    def open_first_product(self):
        browser.element(by.css('a[href*="product"]')).click()

    def add_product_to_card(self):
        browser.element("//button[contains(., 'Добавить в корзину')]").click()
        browser.element(by.css('a[href*="cart"]')).should(have.exact_text('1'))

    def open_shopping_cart(self):
        browser.element("//button[contains(.,'В корзине')]").click()

    def clear_shopping_cart(self):
        browser.element("//button[contains(.,'Удалить выбранные')]").click()
        browser.element(by.css('a[href*="my/orderlist"]')).should(have.exact_text('0Заказы'))


cart_not_logged = CartNotLogged()
