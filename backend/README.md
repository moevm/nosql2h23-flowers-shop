# Инструкция для Linux:
## Загрузка и запуск бд
Скачать файл neo4j.dump из папки backend/data, затем выполнить в терминале следующие команды (в данной инструкции команды выполняются из папки $HOME):
1. mkdir neo4j & mkdir neo4j/backups
2. sudo mv path/to/neo4j.dump ./neo4j/backups/
3. docker run --interactive --tty --rm --volume=$HOME/neo4j/data:/data --volume=$HOME/neo4j/backups:/backups neo4j/neo4j-admin:5.16.0 neo4j-admin database load neo4j --from-path=/backups
4. docker run --publish=7474:7474 --publish=7687:7687 --env NEO4J_AUTH=neo4j/my_password --volume=$HOME/neo4j/data:/data neo4j:5.16.0

## Запуск сервера из папки backend
1. python3 -m venv venv
2. source venv/bin/activate
3. pip install -r requirements.txt
4. python3 app.py

# Инструкция для Windows:
## Загрузка и запуск бд
1. Скачать файл neo4j.dump из папки backend/data
2. Добавить этот файл в проект в приложении Neo4j Desktop  
3. Создать новую БД на основе файла neo4j.dump
4. Установить пароль "my_password"
5. После создания нажать на "Start" и "Open"

## Запуск сервера из папки backend
1. python -m venv venv
2. venv\Scripts\activate
3. pip install -r requirements.txt
4. python app.py
