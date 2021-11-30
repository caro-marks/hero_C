migrations:
	sudo docker-compose run backend python manage.py makemigrations

migrate:
	sudo docker-compose run backend python manage.py migrate

build:
	sudo docker-compose up --build