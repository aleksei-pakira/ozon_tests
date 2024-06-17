from selene import browser, by, have


class TravelPage:
    def open_main_page(self):
        browser.open('/')
        browser.driver.refresh()

    def open_ozon_travel_page(self):
        browser.element(by.link_text('Билеты, отели, туры')).click()

    def open_tours_page(self):
        browser.element('#layoutPage>div.b2>div>div>div:nth-child(1)>div>div:nth-child(6)>div>div:nth-child(4)').click()

    def check_tours_title(self):
        browser.element('#layoutPage').should(have.text('Поиск туров'))


ozon_main_page = TravelPage()
