image_tag = peoplefinder:local

build:
	docker build --tag $(image_tag) .

run:
	docker run -it -v $(CURDIR):/code/ -p 8000:8000 --env-file .env --name peoplefinder $(image_tag)
