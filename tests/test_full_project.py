import allure
from allure_commons.types import Severity
from conftest import setup_browser
from pages.rndnsoft_page import RndSoftPage


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Тест сайта rndn_soft')
@allure.story('Проверка смены на английский язык')
@allure.link('https://github.com', name='Testing')
def test_change_english_language(setup_browser):
    rndsoft_page = RndSoftPage(setup_browser)
    with allure.step("Open start page"):
        rndsoft_page.open_start_page()
    with allure.step("change language"):
        rndsoft_page.change_language()
    with allure.step("check english language on page"):
        rndsoft_page.check_english_language_on_page()


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Тест сайта rndn_soft')
@allure.story('Проверка ИНН на странице реквизитов')
@allure.link('https://github.com', name='Testing')
def test_inn_on_requisites_page(setup_browser):
    rndsoft_page = RndSoftPage(setup_browser)
    with allure.step("Open start page"):
        rndsoft_page.open_start_page()
    with allure.step("go to requisites page"):
        rndsoft_page.requisites_page()
    with allure.step("check inn on requisites page"):
        rndsoft_page.check_inn()


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Тест сайта rndn_soft')
@allure.story('Проверка перехода на страницу Продукты')
@allure.link('https://github.com', name='Testing')
def test_go_to_product_page(setup_browser):
    rndsoft_page = RndSoftPage(setup_browser)
    with allure.step("Open start page"):
        rndsoft_page.open_start_page()
    with allure.step("go to product page"):
        rndsoft_page.go_to_product_page()
    with allure.step("check product page"):
        rndsoft_page.check_product_page()


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Тест сайта rndn_soft')
@allure.story('Проверка наличия вакансии')
@allure.link('https://github.com', name='Testing')
def test_availability_qa_vacancy(setup_browser):
    rndsoft_page = RndSoftPage(setup_browser)
    with allure.step("Open start page"):
        rndsoft_page.open_start_page()
    with allure.step("go to product page"):
        rndsoft_page.go_to_vacancy_page()
    with allure.step("check product page"):
        rndsoft_page.check_availability_qa_vacancy()


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Тест сайта rndn_soft')
@allure.story('Проверка корректного описания вакансии')
@allure.link('https://github.com', name='Testing')
def test_description_qa_vacancy(setup_browser):
    rndsoft_page = RndSoftPage(setup_browser)
    with allure.step("Open start page"):
        rndsoft_page.open_start_page()
    with allure.step("go to product page"):
        rndsoft_page.go_to_vacancy_page()
    with allure.step("check product page"):
        rndsoft_page.check_description_qa_vacancy()


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Тест сайта rndn_soft')
@allure.story('Проверка отправки сообщения со страницы "Компания"')
@allure.link('https://github.com', name='Testing')
def test_sending_message(setup_browser):
    rndsoft_page = RndSoftPage(setup_browser)
    with allure.step("Open start page"):
        rndsoft_page.open_start_page()
    with allure.step("go to company page"):
        rndsoft_page.go_to_company_page()
    with allure.step("fill massage form and submit message"):
        rndsoft_page.fill_and_submit_message_form()
    with allure.step("check sending message success"):
        rndsoft_page.check_sending_message_success()


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Тест сайта rndn_soft')
@allure.story(
    'Проверка отправки сообщения со страницы "Компания" без предоставления согласия с Политикой конфиденциальности')
@allure.link('https://github.com', name='Testing')
def test_sending_message_without_agreement(setup_browser):
    rndsoft_page = RndSoftPage(setup_browser)
    with allure.step("Open start page"):
        rndsoft_page.open_start_page()
    with allure.step("go to company page"):
        rndsoft_page.go_to_company_page()
    with allure.step("fill massage form and submit message without agreement"):
        rndsoft_page.fill_and_submit_message_form_without_agreement()
    with allure.step("check error sending message"):
        rndsoft_page.check_error_sending_message()
