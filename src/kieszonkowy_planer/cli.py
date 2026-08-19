"""Interfejs linii poleceń dla Kieszonkowego Planera."""

from __future__ import annotations

import argparse

from .planner import build_plan, parse_task


def build_parser() -> argparse.ArgumentParser:
    """Utwórz parser argumentów CLI."""

    parser = argparse.ArgumentParser(
        prog="kieszonkowy-planer",
        description="Ułóż prosty plan pracy z listy zadań.",
    )
    parser.add_argument(
        "tasks",
        nargs="*",
        metavar="ZADANIE[:PRIORYTET]",
        help="Zadanie, opcjonalnie z priorytetem, np. 'Napisać testy:1'.",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    """Uruchom aplikację CLI."""

    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        tasks = [parse_task(raw_task) for raw_task in args.tasks]
    except ValueError as exc:
        parser.error(str(exc))

    plan = build_plan(tasks)
    print(plan.render())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
