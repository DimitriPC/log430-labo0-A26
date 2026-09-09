"""
Calculator app tests
SPDX - License - Identifier: LGPL - 3.0 - or -later
Auteurs : Gabriel C. Ullmann, Fabio Petrillo, 2025
"""

from calculator import Calculator

my_calculator = Calculator()

def test_app():
    my_calculator = Calculator()
    welcome_message = my_calculator.get_hello_message()
    assert "== Calculatrice v1.0 ==" in welcome_message

def test_addition():
    assert my_calculator.addition(2, 3) == 5

def test_substraction():
    assert my_calculator.subtraction(5, 2) == 3

def test_multiplication():
    assert my_calculator.multiplication(2, 4) == 8

def test_division():
    assert my_calculator.division(10, 5) == 2

def test_division_by_zero():
    assert my_calculator.division(10, 0).startswith("Erreur")