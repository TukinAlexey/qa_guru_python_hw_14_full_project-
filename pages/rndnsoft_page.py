from time import sleep

from selene import have

from conftest import setup_browser


class Start_page:
    browser = setup_browser

    def open_start_pag(self, setup_browser):
        browser = setup_browser

        browser.open('https://www.rnd-soft.ru/')
        browser.element('[class="button is-primary"]').click()
        browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
            "Мы создаём продукты и проекты. Помогаем нашим клиентам в достижении успеха Присоединяйтесь к команде или пишите для сотрудничества."))

    def change_language(self, setup_browser):
        browser = setup_browser

        browser.element('[data-language-switcher-locale-param="ru"]').click()
        browser.element('[data-language-switcher-locale-param="en"]').click()
        sleep(2)

    def check_english_language_on_page(self, setup_browser):
        browser = setup_browser

        browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
            "We create products and projects. We help our clients succeed Join the team or write to us for cooperation."))

    def requisites_page(self, setup_browser):
        browser = setup_browser

        browser.element('[class="requisites is-size-5 link link--grey-dark"]').click()
        sleep(2)

    def check_inn(self, setup_browser):
        browser = setup_browser

        browser.element('[class="text has-text-grey-dark custom-is-size-body line-height-140"]').should(have.text(
            "6165189197"))
