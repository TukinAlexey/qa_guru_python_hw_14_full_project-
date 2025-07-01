from time import sleep

from conftest import setup_browser

from selene import have
from selene import browser

from pages.rndnsoft_page import Start_page


# Запускаем тест локально в браузере
def test_en_language_browser():
    # Открываем страницу браузера
    browser.open('https://www.rnd-soft.ru/')
    browser.element('[class="button is-primary"]').click()
    browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
        "Мы создаём продукты и проекты. Помогаем нашим клиентам в достижении успеха Присоединяйтесь к команде или пишите для сотрудничества."))

    # Переключаю язык на английский
    browser.element('[data-language-switcher-locale-param="ru"]').click()
    browser.element('[data-language-switcher-locale-param="en"]').click()
    sleep(2)

    # Проверяю что изменился язык на сайте
    browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
        "We create products and projects. We help our clients succeed Join the team or write to us for cooperation."))
    browser.quit()

    # Запускаем тест на селенойде
def test_en_language_selenoid(setup_browser):
    browser = setup_browser

    browser.open('https://www.rnd-soft.ru/')
    browser.element('[class="button is-primary"]').click()
    browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
        "Мы создаём продукты и проекты. Помогаем нашим клиентам в достижении успеха Присоединяйтесь к команде или пишите для сотрудничества."))

    # Переключаю язык на английский

    browser.element('[data-language-switcher-locale-param="ru"]').click()
    browser.element('[data-language-switcher-locale-param="en"]').click()
    sleep(3)

    # Проверяю что изменился язык на сайте
    browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
        "We create products and projects. We help our clients succeed Join the team or write to us for cooperation."))


# Запускаем тест на селенойде с ООП
def test_en_language_selenoid_with_OOP(setup_browser):
    browser = setup_browser
    start_page = Start_page()

    # Открываем стартовую страницу
    start_page.open_start_pag(browser)

    # Переключаю язык на английский
    start_page.change_language(browser)

    # Проверяю что изменился язык на сайте
    start_page.check_english_language_on_page(browser)
