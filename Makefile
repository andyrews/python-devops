install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
req_update:
	pip freeze > requirements.txt
lint: 
	pylint --disable=R,C *.py devopslib