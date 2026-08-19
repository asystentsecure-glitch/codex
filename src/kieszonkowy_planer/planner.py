"""Logika planowania zadań dla przykładowej aplikacji CLI."""

from __future__ import annotations

from dataclasses import dataclass


DEFAULT_PRIORITY = 3


@dataclass(frozen=True, order=True)
class Task:
    """Pojedyncze zadanie z nazwą i priorytetem.

    Niższa liczba oznacza wyższy priorytet, np. `1` jest pilniejsze niż `3`.
    """

    priority: int
    name: str

    def __post_init__(self) -> None:
        if not self.name.strip():
            raise ValueError("Nazwa zadania nie może być pusta.")
        if self.priority < 1:
            raise ValueError("Priorytet musi być liczbą dodatnią.")

    def label(self) -> str:
        """Zwróć czytelną etykietę zadania."""

        return f"P{self.priority}: {self.name}"


@dataclass(frozen=True)
class Plan:
    """Uporządkowany plan pracy."""

    tasks: tuple[Task, ...]

    def render(self) -> str:
        """Zwróć plan jako tekst gotowy do wypisania w terminalu."""

        if not self.tasks:
            return "Brak zadań do zaplanowania."

        lines = ["Plan pracy:"]
        for index, task in enumerate(self.tasks, start=1):
            lines.append(f"{index}. {task.label()}")
        return "\n".join(lines)


def parse_task(raw: str) -> Task:
    """Zamień tekst z CLI na `Task`.

    Format wejściowy to `nazwa:priorytet`, np. `Napisać testy:1`.
    Jeśli priorytet zostanie pominięty, używany jest `DEFAULT_PRIORITY`.
    """

    name, separator, priority_text = raw.rpartition(":")
    if not separator:
        return Task(priority=DEFAULT_PRIORITY, name=raw.strip())

    try:
        priority = int(priority_text)
    except ValueError as exc:
        raise ValueError(f"Nieprawidłowy priorytet w zadaniu: {raw!r}.") from exc

    return Task(priority=priority, name=name.strip())


def build_plan(tasks: list[Task]) -> Plan:
    """Zbuduj plan posortowany według priorytetu, a potem nazwy."""

    return Plan(tasks=tuple(sorted(tasks)))
