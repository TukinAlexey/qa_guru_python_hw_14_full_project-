# Тестовое задание для проекта https://www.rnd-soft.ru/  
## В проекте демонстрируются навыки написания автотестов с применением разметки allure и использованием принципов ООП.
В проекте проверяется:
- Корректная смена языка на странице
- Наличие вакансии "QA-инженер/Тестировщик"
- Описание к вакансии "QA-инженер/Тестировщик"
- Переход на страницу "Продукты"
- Проверка ИНН компании на странице "Реквизиты"

## Продемонстрированы навыки создания инфраструктуры проекта: 
- Создан [билд в jenkins](https://jenkins.autotests.cloud/job/qa_gugu_hw_my_full_project/)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/jenkins.png?raw=true)
- К прогонам в jenkins добавляется [allure отчет](https://jenkins.autotests.cloud/job/qa_gugu_hw_my_full_project/) к которому приложены:
  - Скриншот
  - Логи браузера
  - Ресурс страницы
  - Видео прохождение теста 
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Allure.png?raw=true)
- Кейсы из прогона добавляются в [TestOps](https://allure.autotests.cloud/project/4825/test-cases/38830?treeId=9437)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/TestOps.png?raw=true)
- Прогоны и кейсы из TeasOps добавляются в задачу [Jira](https://jira.autotests.cloud/browse/HOMEWORK-1475)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Cases.png?raw=true)
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Launches.png?raw=true)
- После прогона в телеграм отправляется отчет о прохождении тестов
![image](https://github.com/TukinAlexey/qa_guru_python_hw_14_full_project-/blob/main/files/Bot.png?raw=true)