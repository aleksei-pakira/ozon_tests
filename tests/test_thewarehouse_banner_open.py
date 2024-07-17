from allure_commons.types import Severity
import allure

from ozon_test_project.pages.thewarehouse_banner_open import thewarehouse_main_page
@allure.feature('Open ozon travel tab')
@allure.story('User should be able to open ozon tour tab')
@allure.label('owner', 'aleksei-pakira')
@allure.severity(Severity.BLOCKER)
@allure.title('"ozon tour tab" should be displayed')
def test_open_thewarehouse_banner_page():
    with allure.step('открыть главную страницу'):
        thewarehouse_main_page.open_main_page()

#    with allure.step('открыть ozon travel'):
#        ozon_main_page.open_ozon_travel_page()

#    with allure.step('открыть Поиск туров'):
#        ozon_main_page.open_tours_page()

#    with allure.step('Проверить заголовок "Поиск туров" вкладки'):
#        ozon_main_page.check_tours_title()




