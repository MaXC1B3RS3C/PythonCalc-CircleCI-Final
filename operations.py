import math


def suma(sumand1, sumand2):
    return sumand1+sumand2


def resta(minuendo, sustraendo):
    return minuendo - sustraendo


def multi(mult1, mult2):
    return mult1 * mult2


def div(dividendo, divisor):
    try:
        return dividendo/divisor
    except ZeroDivisionError:
        return math.nan


def factorial(num):
    factorial = 1
    for i in range(1, num+1):
        factorial = factorial*i
    return factorial


def exponente(num):
    res = num
    for i in range(1, num):
        res = res*num
    return res


def square(radicand):
    try:
        return math.sqrt(radicand)
    except ValueError:
        return math.nan
