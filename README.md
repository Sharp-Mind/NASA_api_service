# NASA_api_service

### Language/Язык
- [English](#en_lang)
- [Русский](#ru_lang)
  

## <a name="en_lang"></a> Installation (EN)

1. Copy the repository to your computer
2. Create a new virtual environment next to the repository folder with the command
    ```
    python3 -m venv venv
    ```
3. Activate the virtual environment with the command
    source venv/bin/activate
4. Go to the project folder, from the project folder execute:
    ```
    pip3 -r requirements.txt
    ```
5. After installing all the dependencies, start the local server with the command
    ```
    python3 manage.py runserver
    ```
## Usage

When you navigate to ```localhost:8000```, the page will display a data entry form for the request. The fields "Start date" and "Count of objects" are mandatory. After clicking on the "Get objects" button, a request will be made to the NASA server to display information on request. The result of the execution will be the appearance of a table with the requested data under the query form.

## <a name="ru_lang"></a> Установка (RU)

1. Скопировать репозиторий на свой компьютер
2. Создать новое виртуальное окружение рядом с папкой репозитория командой
   ```
   python3 -m venv venv
   ```
3. Активировать витруальное окружение командой
   source venv/bin/activate
4. Перейтив папку проекта, из папки проекта выполнить:
   ```
   pip3 -r requirements.txt
   ```
5. После установки всех зависимостей, запустить локальный сервер командой
   ```
   python3 manage.py runserver
   ```
## Использование

При переходе по адресу ```localhost:8000``` на странице будет отображена форма ввода данных для запроса. Поля "Start date" и "Count of objects" обязательны к заполнению. После нажания на кнопку "Get objects" будет выполнен запрос к серверу NASA для вывода информации по запросу. Результатом выполнения станет появление под формой запроса таблицы с запрошенными данными.

