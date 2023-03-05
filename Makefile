dev:
	sudo docker-compose -p sotiny -f local.yml up

build:
	sudo docker-compose -p sotiny -f local.yml build

migrations:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py migrate

seed:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py shell < sotinyurl/utils/seed.py

superuser:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py createsuperuser

shell:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py shell

cleardocker:
	sudo docker-compose -p sotiny -f local.yml down --volumes --remove-orphans --rmi all