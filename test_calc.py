import pytest
from app.routers import calculator


class Operands():
    def __init__(self, a, b):
        self.a = a
        self.b = b


def test_add():
    assert calculator.add(Operands(2, 3))["result"] == 5


def test_mul():
    assert calculator.multiply(Operands(2, 3))["result"] == 6


def test_divide():
    assert calculator.divide(Operands(6, 3))["result"] == 2


def test_sub():
    assert calculator.subtract(Operands(3, 1))["result"] == 2
