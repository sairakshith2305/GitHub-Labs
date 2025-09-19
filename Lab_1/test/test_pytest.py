import pytest
from src import calculator

def test_fun1():
    assert calculator.fun1(2, 3) == 5
    assert calculator.fun1(5,0) == 5
    assert calculator.fun1 (-1, 1) == 0
    assert calculator.fun1 (-1, -1) == -2

def test_fun1_floats():
    """Test addition with floating point numbers"""
    assert calculator.fun1(2.5, 3.7) == 6.2
    assert calculator.fun1(0.1, 0.2) == pytest.approx(0.3)
    assert calculator.fun1(-2.5, 1.5) == -1.0
    assert calculator.fun1(3.14159, 2.71828) == pytest.approx(5.85987)


def test_fun1_large_numbers():
    """Test addition with very large numbers"""
    assert calculator.fun1(1e10, 1e10) == 2e10
    assert calculator.fun1(999999999, 1) == 1000000000
    assert calculator.fun1(-1e10, 1e10) == 0


def test_fun2():
    assert calculator.fun2(2, 3) == -1
    assert calculator.fun2(5,0) == 5
    assert calculator.fun2 (-1, 1) == -2
    assert calculator.fun2 (-1, -1) == 0

def test_fun2_floats():
    """Test subtraction with floating point numbers"""
    assert calculator.fun2(5.5, 2.3) == pytest.approx(3.2)
    assert calculator.fun2(0.1, 0.2) == pytest.approx(-0.1)
    assert calculator.fun2(-2.5, -1.5) == -1.0
    assert calculator.fun2(10.0, 0.1) == pytest.approx(9.9)


def test_fun2_large_numbers():
    """Test subtraction with very large numbers"""
    assert calculator.fun2(1e10, 1e9) == 9e9
    assert calculator.fun2(1000000000, 1) == 999999999
    assert calculator.fun2(-1e10, -1e10) == 0


def test_fun3():
    assert calculator.fun3(2, 3) == 6
    assert calculator.fun3(5,0) == 0
    assert calculator.fun3 (-1, 1) == -1
    
    assert calculator.fun3 (-1, -1) == 1

def test_fun3_floats():
    """Test multiplication with floating point numbers"""
    assert calculator.fun3(2.5, 4) == 10.0
    assert calculator.fun3(0.5, 0.5) == 0.25
    assert calculator.fun3(-2.5, 2) == -5.0
    assert calculator.fun3(3.14, 2) == pytest.approx(6.28)
    assert calculator.fun3(0.1, 0.1) == pytest.approx(0.01)


def test_fun4():
    assert calculator.fun4(2, 3, 5) == 10
    assert calculator.fun4(5,0, -1) == 4
    assert calculator.fun4 (-1, -1, -1) == -3
    
    assert calculator.fun4 (-1, -1, 100) == 98

def test_fun4_floats():
    """Test three-number addition with floats"""
    assert calculator.fun4(1.5, 2.5, 3.5) == 7.5
    assert calculator.fun4(0.1, 0.2, 0.3) == pytest.approx(0.6)
    assert calculator.fun4(-1.5, -2.5, 4.0) == 0.0
    assert calculator.fun4(3.14, 2.71, 1.41) == pytest.approx(7.26)
