## ЦЕЛЬ СОЗДАНИЯ
данный репозиторий создан для выполнения тестового задания, цель которого - сделать django app, который будет 
реализовывать древовидное меню на базе templatetag, соблюдая определенные условия.
Выполнял его на базе джанго-бойлерплейта собственной сборки (https://github.com/Delacrua/django-boilerplate)


## ОСОБЕННОСТИ РЕАЛИЗАЦИИ
проект может быть запущен как из докер-контейнера так и локально, в проекте оставлены два docker-compose файла - 
локальный вариант и под деплой (USWGI, раздача статики с помощью Whitenoise) 
Для упрощения начального ознакомления с проектом добавил в него базу с двумя объектами меню и элементами меню 
в каждом из них и вывел оба меню на стартовый экран /menu/.

**администраторский аккаунт - admin / admin**


## ПОСЛЕДОВАТЕЛЬНОСТЬ ЗАПУСКА

1. клонировать репозиторий

   `git clone https://github.com/Delacrua/nested_tree_menu.git`

2. перейти в директорию с проектом 

   `cd nested_tree_menu`

3. в директории /src проекта переименовать файл .env.example в .env


4. Дальнейшие действия зависят от способа запуска:

    4.1. Для локального запуска последовательно выполнить команды:
        
        4.1.1. python -m venv venv (UNIX) 
        или	
        python -m venv venv (Windows)

        4.1.2. source venv/bin/activate (UNIX)
        или
        venv\Scripts\activate (Windows)
    
        4.1.3. pip install -r src/dev-requirements.txt   

        4.1.4. cd src
    
        4.1.5. python manage.py runserver   
        
        4.1.6. Перейти по адресу http://127.0.0.1:8000/menu/

    4.2. Для запуска из докер-контейнера последовательно выполнить команды (требуется установленный docker и docker-compose):
        
        Для запуска локального контейнера
        4.2.1.1. make local-build 

        4.2.1.2. make local-up 

        4.2.1.2. Перейти по адресу http://127.0.0.1:8000/menu/

        Для запуска контейнера под деплой
        4.2.1. make release-build 

        4.2.2. make release-up

        4.2.2. Перейти по адресу http://127.0.0.1:8002/menu/
