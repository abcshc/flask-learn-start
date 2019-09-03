run:
	flask run --host 0.0.0.0
tests:
	pytest
lint:
	pylint flask_app