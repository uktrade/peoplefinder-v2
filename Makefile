image_tag = peoplefinder:local
container_name = peoplefinder

build:
	docker build --tag $(image_tag) .

run:
	docker run --rm -it -v $(CURDIR):/code/ -p 8000:8000 --name $(container_name) $(image_tag)

createsuperuser:
	docker exec -it $(container_name) python manage.py createsuperuser

makemigrations:
	docker exec -it $(container_name) python manage.py makemigrations

migrate:
	docker exec -it $(container_name) python manage.py migrate
