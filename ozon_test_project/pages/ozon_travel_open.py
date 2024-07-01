from selene import browser, by, have, command
import time


class TravelPage:
    def open_main_page(self):
        browser.open('/')
        browser.driver.refresh()
        time.sleep(10)

    def open_ozon_travel_page(self):
        browser.element(by.link_text('Билеты, отели, туры')).click()
#        browser.element(by.partial_link_text("Билеты, отели, туры")).perform(command.js.click)
#        browser.element("//a[contains(text(), 'Билеты, отели, туры')]/..").click()

    def open_tours_page(self):
        browser.element("//span[contains(text(), 'Туры')]/../..").click()       #/../.. - parent/parent

    def check_tours_title(self):
        browser.element('#layoutPage').should(have.text('Поиск туров'))


ozon_main_page = TravelPage()
