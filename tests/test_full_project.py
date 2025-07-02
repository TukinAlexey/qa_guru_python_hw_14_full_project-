from time import sleep

import allure
from allure_commons.types import Severity

from conftest import setup_browser
from pages.rndnsoft_page import Start_page


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Issues_name')
@allure.story('Проверка названия Issue')
@allure.link('https://github.com', name='Testing')
def test_allure_labels():
    pass


def test_english_language(setup_browser):
    browser = setup_browser
    start_page = Start_page()

    # Открываем стартовую страницу
    with allure.step("Open start page"):
        start_page.open_start_pag(browser)

    # Переключаю язык на английский
    with allure.step("change language"):
        start_page.change_language(browser)

    # Проверяю что изменился язык на сайте
    with allure.step("check english language on page"):
        start_page.check_english_language_on_page(browser)


def test_inn_on_requisites_page(setup_browser):
    browser = setup_browser
    start_page = Start_page()

    # Открываем стартовую страницу
    with allure.step("Open start page"):
        start_page.open_start_pag(browser)

    # Переходим на страницу с реквизитами
    with allure.step("go to requisites page"):
        start_page.requisites_page(browser)

    # Проверяем что на странице верно указан ИНН
    with allure.step("check inn on requisites page"):
        start_page.check_inn(browser)