# Przewodnik dla nowych osób

Ten dokument opisuje, jak czytać i rozwijać projekt `Kieszonkowy Planer`.

## 1. Zacznij od modelu domeny

Najważniejsza logika znajduje się w `src/kieszonkowy_planer/planner.py`.

Projekt używa prostego modelu:

- `Task` reprezentuje pojedyncze zadanie,
- `Plan` reprezentuje uporządkowaną listę zadań,
- `build_plan()` sortuje zadania według priorytetu,
- `parse_task()` zamienia tekst z CLI na obiekt `Task`.

## 2. Potem sprawdź wejście programu

Plik `src/kieszonkowy_planer/cli.py` jest cienką warstwą nad logiką z `planner.py`. Dzięki temu łatwiej testować reguły biznesowe bez uruchamiania terminala.

## 3. Na końcu przeczytaj testy

Testy w `tests/test_planner.py` pokazują najważniejsze przypadki:

- parsowanie zadania z priorytetem,
- domyślny priorytet,
- walidację pustych nazw,
- sortowanie planu,
- formatowanie wyjścia.

## Typowy workflow

Najprostszy workflow korzysta z komend z `Makefile`:

```bash
make test
make run
```

Te same kroki można wykonać bez `make`:

```bash
PYTHONPATH=src python -m unittest discover -s tests
PYTHONPATH=src python -m kieszonkowy_planer.cli "Dodać funkcję:1" "Napisać dokumentację:2"
```

## Pomysły na dalszy rozwój

- zapis planu do pliku JSON,
- oznaczanie zadań jako wykonane,
- filtrowanie zadań po tagach,
- kolorowe wyjście w terminalu,
- konfiguracja domyślnego priorytetu.
