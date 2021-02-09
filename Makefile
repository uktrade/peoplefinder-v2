image_tag = peoplefinder:local
container_name = peoplefinder

build:
	docker build --tag $(image_tag) .

run:
	docker run -it -v $(CURDIR):/code/ -p 8000:8000 --env-file .env --name $(container_name) $(image_tag)

createsuperuser:
	docker exec -it $(container_name) python manage.py createsuperuser
