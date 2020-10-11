# stepik-homework
Домашние работы по курсу https://stepik.org/course/575/syllabus

**Пожалуйста, используйте --tb=line, чтобы было видно assert**

pytest -v --tb=line --language=es test_items.py  - запуск по умолчанию (в хроме)

pytest -v --tb=line --browser_name=firefox --language=es test_items.py - запуск в мозиле

pytest -v --tb=line --browser_name=chrome --language=es test_items.py - запуск с явным указанием хрома

pytest -v --tb=line --language=fr test_items.py - для проверки "Ajouter au panier"
