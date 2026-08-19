import unittest

from kieszonkowy_planer.planner import DEFAULT_PRIORITY, Task, build_plan, parse_task


class ParseTaskTests(unittest.TestCase):
    def test_parse_task_with_priority(self) -> None:
        task = parse_task("Napisać testy:1")

        self.assertEqual(task.name, "Napisać testy")
        self.assertEqual(task.priority, 1)

    def test_parse_task_uses_default_priority(self) -> None:
        task = parse_task("Zrobić herbatę")

        self.assertEqual(task.name, "Zrobić herbatę")
        self.assertEqual(task.priority, DEFAULT_PRIORITY)

    def test_parse_task_rejects_invalid_priority(self) -> None:
        with self.assertRaises(ValueError):
            parse_task("Napisać dokumentację:pilne")


class TaskTests(unittest.TestCase):
    def test_task_rejects_empty_name(self) -> None:
        with self.assertRaises(ValueError):
            Task(priority=1, name="   ")

    def test_task_rejects_non_positive_priority(self) -> None:
        with self.assertRaises(ValueError):
            Task(priority=0, name="Napisać README")


class BuildPlanTests(unittest.TestCase):
    def test_build_plan_sorts_by_priority_and_name(self) -> None:
        plan = build_plan(
            [
                Task(priority=2, name="Dokumentacja"),
                Task(priority=1, name="Testy"),
                Task(priority=1, name="Architektura"),
            ]
        )

        self.assertEqual(
            [task.name for task in plan.tasks],
            ["Architektura", "Testy", "Dokumentacja"],
        )

    def test_render_empty_plan(self) -> None:
        plan = build_plan([])

        self.assertEqual(plan.render(), "Brak zadań do zaplanowania.")

    def test_render_plan(self) -> None:
        plan = build_plan([Task(priority=1, name="Testy")])

        self.assertEqual(plan.render(), "Plan pracy:\n1. P1: Testy")


if __name__ == "__main__":
    unittest.main()
