import pytest

from app.calculator import Calculator
class TestCalc:
    def setup(self):
        self.calc = Calculator

    # Сложение метод калькулятора (было в юните, но изменены данные, согласно д/з)
    def test_adding_success(self):
        assert self.calc.adding(self,18,82) == 100
    # тест был в юните (негативный тест)
    def test_adding_unsuccess(self):
        assert self.calc.adding(self,1,1) == 3
    # тест был в юните
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(self,1,0)
    # Домашенее задание
    # Вычитание метод калькулятора
    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 20, 16) == 4

    # Деление метод калькулятора
    def test_division_success(self):
        assert self.calc.division(self, 49, 7) == 7
    # Деление нуля на число
    def test_division_zero_on(self):
        assert self.calc.division(self, 0, 25) == 0

    # Умножение метод калькулятора
    def test_multiply_success(self):
        assert self.calc.multiply(self, 10, 2) == 20
    # Умножение на ноль
    def test_zero_multiply(self):
        assert self.calc.multiply(self, 125, 0) == 0
        assert self.calc.multiply(self, 0, 15) == 0

    def teardown(self):
        print('Выполнение метода Teardown')

