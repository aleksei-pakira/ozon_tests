from selene import browser, by, have, be


class CartNotLogged:
    def open_main_page(self):
        browser.open('/')
        browser.driver.refresh()

    def check_items_quantity_in_cart(self):
        browser.element(by.css('a[href*="cart"]')).should(have.text("0")) and (have.text("Корзина"))

    def open_first_product(self):
        browser.element(by.css('a[href*="product"]')).click()

    def add_product_to_card(self):
        browser.element("//button[contains(., 'Добавить в корзину')]").click()
#        browser.wait.until(lambda: browser.element(by.css('a[href*="cart"]')).text == '1')
 #       browser.element(by.css('a[href*="cart"]')).should(have.text("1")).should(be.visible, timeout=5)
        #browser.wait.until(browser.element('//div[@id="myDiv"]').is_visible, timeout=10)

        #text_field.send_keys("Первая строка", Keys.ENTER, "Вторая строка", Keys.ENTER, "Третья строка")
        #should(have.text('''
       # Привет,
        #это текст
        #на двух строках
        #'''))

    def open_shopping_cart(self):
        browser.element("//button[contains(.,'В корзине')]").click()

    def clear_shopping_cart(self):
        browser.element("//button[contains(.,'Удалить выбранные')]").click()
        browser.element(by.css('a[href*="cart"]')).should(have.text("0") and (have.text("Корзина")))


cart_not_logged = CartNotLogged()
