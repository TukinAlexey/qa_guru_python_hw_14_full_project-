# Дипломный проект UI на основе сайта https://www.rnd-soft.ru/  
## В проекте демонстрируются навыки написания UI автотестов с применением разметки allure, использование принципов ООП, интеграция с jenkins и TestOps
В проекте проверяется:
- Корректная смена языка на странице
- Наличие вакансии "QA-инженер/Тестировщик"
- Описание к вакансии "QA-инженер/Тестировщик"
- Переход на страницу "Продукты"
- Проверка ИНН компании на странице "Реквизиты"
- Заполнение формы сообщения и его отправка на странице "Компания"
- Ошибка при отправке сообщения без проставления чек-бокса согласия с Политикой конфиденциальности

## Продемонстрированы навыки создания инфраструктуры проекта: 
- Создан [билд в jenkins](https://jenkins.autotests.cloud/job/qa_gugu_hw_my_full_project/)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Jenkins_1.png)
- К прогонам в jenkins добавляется [allure отчет](https://jenkins.autotests.cloud/job/qa_gugu_hw_my_full_project/26/allure/#suites) к которому приложены:
  - Скриншот
  - Логи браузера
  - Ресурс страницы
  - Видео прохождение теста 
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Allure_1.png)
- Кейсы из прогона добавляются в [TestOps](https://allure.autotests.cloud/project/4825/test-cases/38830?treeId=9437)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/TestOps_1.png)
- Настроен запуск автотестов из TestOps
- После прогона в телеграм отправляется отчет о прохождении тестов
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Telegram_1.png)