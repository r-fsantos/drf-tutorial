# drf-tutorial

## Simple credentials

```
username: admin
password: admin
```

## Expected initial project folder structure

```bash
.
./tutorial
./tutorial/asgi.py
./tutorial/__init__.py
./tutorial/quickstart
./tutorial/quickstart/migrations
./tutorial/quickstart/migrations/__init__.py
./tutorial/quickstart/models.py
./tutorial/quickstart/__init__.py
./tutorial/quickstart/apps.py
./tutorial/quickstart/admin.py
./tutorial/quickstart/tests.py
./tutorial/quickstart/views.py
./tutorial/settings.py
./tutorial/urls.py
./tutorial/wsgi.py
./LICENSE
./requirements.txt
./db.sqlite3
./README.md
./run_time.txt
./.gitignore
./manage.py
./venv
./.git
```

- App created within the project directory. Using the project's namespace avoids name clashes with external modules. (Doubt...)
