import time
from selene import browser, by, have
import requests


class CartNotLogged:
    def open_main_page(self):
        browser.open('/')
        browser.driver.refresh()

    def check_items_quantity_in_cart(self):
        browser.element(by.css('a[href*="cart"]')).should(have.text("0")) and (have.text("Корзина"))

    def open_first_product(self):
 #       browser.element(by.css('a[href*="product"]')).click()
        browser.element("//*[starts-with(text(), 'О! Распродажа')]").click()
#        browser.element('# layoutPage > div.b3 > div.d1w_9 > div > div > div:nth-child(7) > div > div:nth-child(15) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(17) > a')
        # layoutPage > div.b3 > div.d1w_9 > div > div > div:nth-child(7) > div > div:nth-child(15) > div > div > div:nth-child(1) > div:nth-child(1) > div > div:nth-child(17) > a

    def add_product_to_card(self):
#        browser.element("//button[contains(., 'Добавить в корзину')]").click()
        browser.element('("//*[contains(text(), "Добавить в корзину")]")')
        time.sleep(5)
        response2 = requests.request("POST", url2)

        assert response2.status_code == 403

#    def test_ozon_cart_api(self):
#        response2 = requests.request("POST", url2)

 #       assert response2.status_code == 403




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
        browser.element('("//*[contains(text(), "В корзине")]")')

    def clear_shopping_cart(self):
        browser.element("//button[contains(.,'Удалить выбранные')]").click()
        browser.element(by.css('a[href*="cart"]'))
 #       browser.element(by.css('a[href*="cart"]')).click()
#        browser.element('("//*[contains(text(), "1", "Корзина")]")')
#        browser.element(by.css('a[href*=/cart/]')).should(have.text("0")) and (have.text("Корзина"))
 #       browser.element(by.link_text('cart')).click()


cart_not_logged = CartNotLogged()

url2 = "https://ozon.ru/api/composer-api.bx/_action/addToCart"
response2 = requests.request("POST", url2)

