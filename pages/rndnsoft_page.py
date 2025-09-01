from selene import have, be


class RndSoftPage:
    def __init__(self, browser):
        self.browser = browser

    def open_start_page(self):
        self.browser.open('https://www.rnd-soft.ru/')
        self.browser.element('[class="button is-primary"]').click()
        self.browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
            "Мы создаём продукты и проекты. Помогаем нашим клиентам в достижении успеха Присоединяйтесь к команде или пишите для сотрудничества."))

    def change_language(self):
        self.browser.element('[data-language-switcher-locale-param="ru"]').click()
        self.browser.element('[data-language-switcher-locale-param="en"]').click()

    def check_english_language_on_page(self):
        self.browser.element('[class="has-text-white-ter has-text-weight-light"]').should(have.exact_text(
            "We create products and projects. We help our clients succeed Join the team or write to us for cooperation."))

    def requisites_page(self):
        self.browser.element('[class="requisites is-size-5 link link--grey-dark"]').click()

    def check_inn(self):
        self.browser.element('[class="text has-text-grey-dark custom-is-size-body line-height-140"]').should(have.text(
            "6165189197"))

    def go_to_product_page(self):
        self.browser.element('[data-action="click->burger-menu#toggleBurgerMenu"]').click()
        self.browser.element('//*[contains(text(),"Продукты")]').click()

    def check_product_page(self):
        self.browser.element('.products .is-hidden-mobile h1').should(have.exact_text(
            "Продукты"))

    def go_to_vacancy_page(self):
        self.browser.element('[data-action="click->burger-menu#toggleBurgerMenu"]').click()
        self.browser.element('//*[contains(text(),"Вакансии")]').click()

    def check_availability_qa_vacancy(self):
        self.browser.element(
            '#vacancy_8 > .name.is-flex.is-align-items-center.is-justify-content-space-between > p').should(
            have.exact_text(
                "QA-инженер/Тестировщик"))

    def check_description_qa_vacancy(self):
        self.browser.element(
            '[class="is-size-5-tablet custom-is-size-body--mobile has-text-white is-family-sans-serif line-height-140"]').should(
            have.exact_text(
                "Мы не стоим на месте: используем современные подходы к разработке, заботимся о безопасности, ценим гибкость и умеем работать командой. И сейчас ищем того, кто усилит нас в роли QA инженера."))

    def go_to_company_page(self):
        self.browser.element('[data-action="click->burger-menu#toggleBurgerMenu"]').click()
        self.browser.element('//*[contains(text(),"Компания")]').click()

    def fill_and_submit_message_form(self):
        self.browser.element('[placeholder="Имя*"]').type('Ivan')
        self.browser.element('[placeholder="Электронная почта*"]').type('dobryden@mail.ru')
        self.browser.element('[placeholder="Сообщение*"]').type('Добрый день')
        self.browser.element('#feedback_agreement').click()
        self.browser.element('[type="submit"]').click()

    def check_sending_message_success(self):
        self.browser.element('//h2[text()="Отправлено!"]').should(be.visible)

    def fill_and_submit_message_form_without_agreement(self):
        self.browser.element('[placeholder="Имя*"]').type('Ivan')
        self.browser.element('[placeholder="Электронная почта*"]').type('dobryden@mail.ru')
        self.browser.element('[placeholder="Сообщение*"]').type('Добрый день')
        self.browser.element('[type="submit"]').click()

    def check_error_sending_message(self):
        self.browser.element('[class="is-size-6 line-height-120 has-text-danger mt-1"]').should(have.exact_text(
            "Чекбокс не может быть неотмеченным"))
