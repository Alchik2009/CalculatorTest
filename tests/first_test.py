import pytest
from app.calculator import Calculator

# Позитивные тесты
class TestCalcCorrectly():
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correctly(self):
    # Проверяем функцию умножения.
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division(self):
    # Проверяем функцию деления.
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction(self):
    # Проверяем функцию вычитания.
        assert self.calc.subtraction(self, 8, 6) == 2

    def test_adding(self):
    # Проверяем функцию сложения.
        assert self.calc.adding(self, 3, 2) == 5

#Негативные тесты
class TestCalcUnCorrectly():
    def setup(self):
    # Запускаем калькулятор
        self.calc = Calculator

    def test_multiply_calculate_uncorrectly(self):
    # Проверяем функцию умножения.
        assert self.calc.multiply(self, 2, 3) == 5

    def test_division_uncorrectly(self):
    # Проверяем функцию деления.
        assert self.calc.division(self, 10, 2) != 5

    def test_subtraction_uncorrectly(self):
    # Проверяем функцию вычитания.
        assert self.calc.subtraction(self, 8, 6) != 2

    def test_adding_uncorrectly(self):
    # Проверяем функцию сложения.
        assert self.calc.adding(self, 3, 2) != 5