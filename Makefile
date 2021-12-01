migrations:
	sudo docker-compose run backend python manage.py makemigrations

migrate:
	sudo docker-compose run backend python manage.py migrate

test:
	sudo docker-compose run backend python manage.py test

build:
	sudo docker-compose up --build -d db
	sudo docker-compose up --build -d backend