#5 lab

1. Створив папки та копіював туди файли.
2. Виконав команди
        pipenv --python 3.7
        pipenv install -r requirements.txt
        pipenv run python app.py
3. запустив виконання тестів за допомогою команди:
        pipenv run pytest test_app.py --url http://localhost:5000

4. Сервер запустився видавши помилки. омилки виправлені шляхом встановлення `redis`
 наступними командами
        sudo apt-get install redis-server
        sudo systemctl enable redis-server.servicе
Після чого вказав для нього адресу у файл `hosts`, після цього все почало працювати.
5. Видалив усі після запуску файли.
6. Знайомлююсь із вмістом `Dockerfile` та `Makefile` та його директивами.
    * `STATES` та `REPO` це змінні, що містять назви тегів та назву репозиторія відповідно;
    * Директива `.PHONY` підставляє значення з змінної `STATES` та викликає директиву `$(STATES)`;
    * `$(STATES)` можна викликати просто підставляючи назву тегу і призначена для білду Docker Image;
    * `run` для запуску сайту та `redis`;
    * `test-app` для запуску тестів;
    * `docker-prune` для очищення ресурсів Docker;

