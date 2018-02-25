.PHONY: check clean install run

check:
	pep8 *.py --filename=*.py

clean:
	rm -r __pycache__
	find . -type f -name '*.pyc' -delete

install:
	pip install -r requirements.txt

run:
	python image_search.py
