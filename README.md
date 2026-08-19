# Kieszonkowy Planer

Kieszonkowy Planer to mały, przykładowy projekt w Pythonie pokazujący, jak może wyglądać uporządkowana baza kodu dla prostego narzędzia CLI. Aplikacja przyjmuje listę zadań, priorytetyzuje je i drukuje czytelny plan pracy.

Projekt jest celowo niewielki: ma kod aplikacji, testy, dokumentację, konfigurację pakietu i przykład użycia. Dzięki temu nadaje się jako punkt startowy dla nowych osób uczących się struktury repozytorium.

## Struktura projektu

```text
.
├── docs/
│   └── getting-started.md
├── src/
│   └── kieszonkowy_planer/
│       ├── __init__.py
│       ├── cli.py
│       └── planner.py
├── tests/
│   └── test_planner.py
├── .gitignore
├── LICENSE
├── pyproject.toml
└── README.md
```

## Wymagania

- Python 3.10 lub nowszy
- Opcjonalnie: `pip` i `venv`, jeśli chcesz zainstalować projekt lokalnie

Projekt nie wymaga zewnętrznych zależności uruchomieniowych.

## Szybki start

Utwórz środowisko wirtualne:

```bash
python -m venv .venv
source .venv/bin/activate
```

Zainstaluj projekt w trybie edytowalnym:

```bash
python -m pip install -e .
```

Uruchom aplikację:

```bash
kieszonkowy-planer "Napisać README:2" "Dodać testy:1" "Wypić kawę:3"
```

Możesz też uruchomić moduł bez instalacji:

```bash
PYTHONPATH=src python -m kieszonkowy_planer.cli "Napisać README:2" "Dodać testy:1"
```

## Testy

Testy korzystają ze standardowego modułu `unittest`, więc nie trzeba instalować dodatkowych narzędzi:

```bash
PYTHONPATH=src python -m unittest discover -s tests
```

## Co warto przejrzeć najpierw?

1. `README.md` — ogólny opis projektu i najważniejsze komendy.
2. `docs/getting-started.md` — przewodnik krok po kroku dla nowych osób.
3. `src/kieszonkowy_planer/planner.py` — logika biznesowa aplikacji.
4. `src/kieszonkowy_planer/cli.py` — warstwa CLI, czyli wejście użytkownika i drukowanie wyniku.
5. `tests/test_planner.py` — przykłady oczekiwanego działania kodu.
