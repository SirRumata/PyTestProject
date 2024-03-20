"""ИМПОРТ"""
# pip freeze > requirements.txt - команда формирования этого файла
# основные эелементы окружения:
# pip install selenium - библиотека selenium для взаимодействия с браузером
# pip install pytest - библиотека pytest для конфигурации тестов
# pip install webdriver-manager - библиотека для автоматической загрузки вебдрайвера
# различные плагины для pytest:
# allure-pytest - отображение результатов прохождения тестов в фреймворке allure
# pytest-selenium - доп возможности по работе с селениум
# pytest-timeout - возможность выставления таймеров глобально\индивидуально для тестов через марки
# pytest-xdist - позхволяет тестам проходить параллельно
# pytest-stress - зацикливание тестов
# pytest-rerunfailures - перезапуск упавших тестов с заданным колличеством попыток
# @pytest.hookimpl(tryfirst\trylast\hookwrapper=true) - фикстура для разграничения хуков из плагинов
# прочее
# selene - библиотека для упрощения взаимодействия с selenium
# requests - для отправки http запросов при тесте api
# pydantic - определение и проверка данных
# sqlalchemy - взаимодействие с БД
# mimesis - библиотека генерации тестовых данных
# black - форматтер кода для поддержания единообразного стиля кода
# flake8 - линтер кода для выявления ошибок в коде
# отчеты:
# pytest-html

"""АЛЛЮР ДОКЕР"""
# pytest --alluredir=allure-results
# docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 ^ -v "%cd%/allure-results:/app/allure-results" ^ -v "%cd%/allure-reports:/app/default-reports" ^ frankescobar/allure-docker-service
# docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 ^ -v "C:/Users/Rumata/PycharmProjects/PythonTestProject/test_saucedemo/allure-results:/app/allure-results" ^ -v "C:/Users/Rumata/PycharmProjects/PythonTestProject/test_saucedemo/allure-reports:/app/default-reports" ^ frankescobar/allure-docker-service
# http://localhost:5050/allure-docker-service/projects/default/reports/1/index.html#

"""ЛОГИ"""
# pytest --html=pytest_html_log.html

"""ЧЕРНОВИЧОК"""
# wait = WebDriverWait(browser, 10) # ожидание 1 секунда
# driver.quit() # закрытие окон после тестов

"""ГИТ"""
# git init
# git config --global user.name "Your Name"
# git config --global user.email "you@example.com"
# git clone https://github.com/your-username/your-repo.git -b main
# git remote add origin https://github.com/your-username/your-repo.git
# git pull
# git add .
# git commit -m "Initial commit"
# git push -u origin master