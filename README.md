Payform

О проекте:
    - python selenium e2e тесты
    - применен page object паттерн
    - используется pytest + unittest + allure фреймворк 
    - запуск в Chrome браузере (есть возможность запускать и в других)
    
Установка:
    - установить java https://www.java.com/ru/download/   
    - установить python 3.9 https://www.python.org/download
    - установить git и сгенерировать ключи в SHA256 и добавить публичный ключ в gitlab
    - скачать chromedriver https://chromedriver.chromium.org/downloads и положить в папку с проектом
    - стянуть проект из репозитория
    - установить pip 

Локальный запуск тестов: 
    - перейти в папку tests
    - для запуска конкретного текста выполнить команду pytest -vv {название теста}
    или текста помощью встроенного ранера IDE по кнопке run 
    - упавшие тесты логируются и отчеты сохраняются в папке allure-results

Запуск в gitlab CI:
    - перейти в pipelines
    - выбрать ветку и нажать Run
