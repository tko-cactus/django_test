up:
	docker-compose up
	
down:
	docker-compose down

shell:
	docker-compose exec web bash

makemigrations:
	docker-compose run --rm web python3 manage.py makemigrations

migrate:
	docker-compose run --rm web python3 manage.py migrate

createsuperuser:
	docker-compose run --rm web python3 manage.py createsuperuser
