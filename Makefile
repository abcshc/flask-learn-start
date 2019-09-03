run:
	env FLASK_APP=run.py flask run
tests:
	pytest
lint:
	pylint flask_app