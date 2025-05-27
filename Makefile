runserver-local:
	uv run manage.py runserver 0.0.0.0:9090 --settings=settings.development


makemigrations:
	uv run manage.py makemigrations --settings=settings.development

migrate:
	uv run manage.py migrate --settings=settings.development

runserver-prod:
	uv run manage.py runserver 0.0.0.0:9090 --settings=settings.production

shell:
	uv run manage.py shell --settings=settings.development