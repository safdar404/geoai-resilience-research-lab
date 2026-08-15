.PHONY: install test api
install:
	python -m pip install -e ".[api,test]"
test:
	pytest -q
api:
	uvicorn api.main:app --reload
