setup:
	virtualenv --python python3 venv
	venv/bin/pip install -r requirements-dev.txt

migrate:
	venv/bin/python manage.py migrate

run: migrate
	venv/bin/python manage.py runserver

shell:
	venv/bin/python manage.py shell

test:
	venv/bin/pytest
