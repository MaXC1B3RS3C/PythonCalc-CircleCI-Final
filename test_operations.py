import math
import operations


def test_suma():
    assert operations.suma(3, 3) == 6
    assert operations.suma(0, 0) == 0
    assert operations.suma(3, -3) == 0
    assert operations.suma(1, -1) == 0


def test_resta():
    assert operations.resta(3, 3) == 0
    assert operations.resta(0, 0) == 0
    assert operations.resta(1, 1) == 0
    assert operations.resta(-3, -3) == 0


def test_multi():
    assert operations.multi(2, 2) == 4
    assert operations.multi(1, 2) == 2
    assert operations.multi(0, 0) == 0
    assert operations.multi(0, 1) == 0
    assert operations.multi(3, 3) == 9


def test_div():
    assert operations.div(2, 2) == 1
    assert math.isnan(operations.div(0, 0))
    assert operations.div(1, 1) == 1
    assert operations.div(3, 3) == 1


def test_factorial():
    assert operations.factorial(2) == 2
    assert operations.factorial(3) == 6
    assert operations.factorial(1) == 1


def test_exponente():
    assert operations.exponente(2) == 4
    assert operations.exponente(4) == 256
    assert operations.exponente(0) == 0


def test_square():
    assert operations.square(4) == 2
    assert operations.square(16) == 4
    assert operations.square(25) == 5
