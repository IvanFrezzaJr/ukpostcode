clean:
	@find ./ -name '*.pyc' -exec rm -f {} \;
	@find ./uk_postcode/ -name '__pycache__' -exec rm -d {} \;
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -rf .pytest_cache

install:
	pip install -e .

test:
	pytest
