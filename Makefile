migrations:
	sudo docker-compose run backend python manage.py makemigrations

migrate:
	sudo docker-compose run backend python manage.py migrate

test:
	sudo docker-compose run backend python manage.py test

populate:
sudo docker-compose run backend python filler.py

build:
	sudo docker-compose up --build -d db
	sudo docker-compose up --build -d backend