import allure
from allure_commons.types import Severity
from conftest import setup_browser
from pages.rndnsoft_page import Rndsoft_page


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Issues_name')
@allure.story('Проверка названия Issue')
@allure.link('https://github.com', name='Testing')
def test_allure_labels():
    pass


def test_change_english_language(setup_browser):
    browser = setup_browser
    rndsoft_page = Rndsoft_page()

    # Открываем стартовую страницу
    with allure.step("Open start page"):
        rndsoft_page.open_start_pag(browser)

    # Переключаю язык на английский
    with allure.step("change language"):
        rndsoft_page.change_language(browser)

    # Проверяю что изменился язык на сайте
    with allure.step("check english language on page"):
        rndsoft_page.check_english_language_on_page(browser)


def test_inn_on_requisites_page(setup_browser):
    browser = setup_browser
    rndsoft_page = Rndsoft_page()

    # Открываем стартовую страницу
    with allure.step("Open start page"):
        rndsoft_page.open_start_pag(browser)

    # Переходим на страницу с реквизитами
    with allure.step("go to requisites page"):
        rndsoft_page.requisites_page(browser)

    # Проверяем что на странице верно указан ИНН
    with allure.step("check inn on requisites page"):
        rndsoft_page.check_inn(browser)


def test_go_to_product_page(setup_browser):
    browser = setup_browser
    rndsoft_page = Rndsoft_page()

    # Открываем стартовую страницу
    with allure.step("Open start page"):
        rndsoft_page.open_start_pag(browser)

    # Переходим на страницу "Продукты"
    with allure.step("go to product page"):
        rndsoft_page.go_to_product_page(browser)

    # Проверяем что мы находимся на странице "Продукты"
    with allure.step("check product page"):
        rndsoft_page.check_product_page(browser)


def test_availability_qa_vacancy(setup_browser):
    browser = setup_browser
    rndsoft_page = Rndsoft_page()

    # Открываем стартовую страницу
    with allure.step("Open start page"):
        rndsoft_page.open_start_pag(browser)

    # Переходим на страницу "Вакансии"
    with allure.step("go to product page"):
        rndsoft_page.go_to_vacancy_page(browser)

    # Проверяем наличие вакансии "QA-инженер/Тестировщик"
    with allure.step("check product page"):
        rndsoft_page.check_availability_qa_vacancy(browser)


def test_description_qa_vacancy(setup_browser):
    browser = setup_browser
    rndsoft_page = Rndsoft_page()

    # Открываем стартовую страницу
    with allure.step("Open start page"):
        rndsoft_page.open_start_pag(browser)

    # Переходим на страницу "Вакансии"
    with allure.step("go to product page"):
        rndsoft_page.go_to_vacancy_page(browser)

    # Проверяем описание вакансии "QA-инженер/Тестировщик"
    with allure.step("check product page"):
        rndsoft_page.check_description_qa_vacancy(browser)
