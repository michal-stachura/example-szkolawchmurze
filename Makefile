dev:
	docker-compose -p sotiny -f local.yml up

build:
	docker-compose -p sotiny -f local.yml build

migrations:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py makemigrations

migrate:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py migrate

seed:
	docker-compose -p sotiny -f local.yml build; \
	docker-compose -p sotiny -f local.yml run --rm django python manage.py migrate; \
	docker-compose -p sotiny -f local.yml run --rm django python manage.py shell < sotinyurl/utils/seed.py

superuser:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py createsuperuser

shell:
	docker-compose -p sotiny -f local.yml run --rm django python manage.py shell

bash:
	docker-compose -p sotiny -f local.yml exec celeryworker bash

cleardocker:
	docker-compose -p sotiny -f local.yml down --volumes --remove-orphans --rmi all