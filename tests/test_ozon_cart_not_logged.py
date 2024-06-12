from allure_commons.types import Severity
import allure

from ozon_test_project.pages.ozon_cart_not_logged import cart_not_logged
@allure.feature('Open ozon travel tab')
@allure.story('User should be able to open ozon tour tab')
@allure.label('owner', 'aleksei-pakira')
@allure.severity(Severity.BLOCKER)
@allure.title('"ozon tour tab" should be displayed')
@allure.link('https://ozon.ru/travel', name='ozon')
def test_add_to_cart_not_logged():
    with allure.step('открыть главную страницу'):
        cart_not_logged.open_main_page()

    with allure.step('проверить,что количестово товаров в коазине = 0'):
        cart_not_logged.check_items_quantity_in_cart()

    with allure.step('страница продукта'):
        cart_not_logged.open_first_product()

    with allure.step('добавить продукт в корзину'):
        cart_not_logged.add_product_to_card()

    with allure.step('открыть корзину'):
        cart_not_logged.open_shopping_cart()

    with allure.step('очистить корзину'):
        cart_not_logged.clear_shopping_cart()

