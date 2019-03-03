osrequirements:
	sudo apt-get install python3-dev libmysqlclient-dev

setup:
	pipenv --python 3.7.2
	pipenv install --dev

migrate:
	pipenv run python manage.py migrate

run: migrate
	pipenv run python manage.py runserver

shell:
	pipenv run python manage.py shell

test: clear
	pipenv run pytest

clear:
	find . -name "*.pyc" -exec rm -rf {} \;
