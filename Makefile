.PHONY: help install run test

help:
	@echo "Dostępne komendy:"
	@echo "  make install  - zainstaluj projekt lokalnie w trybie edytowalnym"
	@echo "  make run      - uruchom przykładowy plan"
	@echo "  make test     - uruchom testy jednostkowe"

install:
	python -m pip install -e .

run:
	PYTHONPATH=src python -m kieszonkowy_planer.cli "Napisać README:2" "Dodać testy:1" "Wypić kawę:3"

test:
	PYTHONPATH=src python -m unittest discover -s tests
