from selene import browser, by, have
import time


class TravelPage:
    def open_main_page(self):
        browser.open('/')
        browser.driver.refresh()
        time.sleep(5)

    def open_ozon_travel_page(self):
#        browser.element(by.link_text('Билеты, отели, туры')).click()
        browser.element(by.partial_link_text('a[href="https://www.ozon.ru/travel/?mwc_campaign=oztravel_horizontal-menu_flight"]')).click()
        time.sleep(5)

    def open_tours_page(self):
        browser.element("//span[contains(text(), 'Туры')]/../..").click()       #/../.. - parent/parent

    def check_tours_title(self):
        browser.element('#layoutPage').should(have.text('Поиск туров'))


ozon_main_page = TravelPage()
