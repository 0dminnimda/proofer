from __future__ import annotations

from typing import Callable, Tuple


class Evaluatable:
    def _evaluate(self, args: ARGS) -> Evaluatable:
        raise NotImplementedError

    def __call__(self, *args: Evaluatable) -> Evaluatable:
        result = self._evaluate(args)
        assert type(result) == Symbol
        return result


class Symbol(Evaluatable):
    name: str

    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return type(self).__name__ + f"({self.name!r})"

    def __str__(self) -> str:
        return "<" + self.name + ">"

    def _evaluate(self, args: ARGS) -> Evaluatable:
        return self


ARGS = Tuple[Evaluatable, ...]
FUNCTION = Callable[[ARGS], Evaluatable]


class Operation(Evaluatable):
    function: FUNCTION

    def __init__(self, function: FUNCTION) -> None:
        self.function = function  # type: ignore

    def __repr__(self) -> str:
        return type(self).__name__ + f"({self.function!r})"

    def __str__(self) -> str:
        return self.function.__name__ + "(" + "" + ")"

    def _evaluate(self, args: ARGS) -> Evaluatable:
        return self.function(*args)
