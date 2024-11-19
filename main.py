#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Übungsblatt 06"""


# Aufgaben 1 und 2

def calculate_digit_sum(number):
    """Calculate digit sum of number

    The digit sum of a natural number is the sum of all its digits. It
    is being calculated by looping over the digits and adding them one
    by one.

    :param number: Positive integer
    :type number: int
    :return: Digit sum of number
    :rtype: int
    """
    try:
        number = str(number)
        digit_sum = 0
        for digit in number:
            digit = int(digit)
            digit_sum += digit
        return digit_sum
    except ValueError:
        return None


# Aufgabe 3

def multiple_digit_sum_iterative(number):
    """Repetitively calculate digit sum

    Repeat the calculation of the digit sum by using the previously
    calculated digit sum as the new number. In the end, only one digit
    is left.

    :param number: Positive integer
    :type number: int
    :return: Final digit of repetitive calculation of digit sum
    :rtype: int
    """

    digit_sum = number
    while digit_sum > 9:
        digit_sum = calculate_digit_sum(digit_sum)
    return digit_sum


def multiple_digit_sum_recursive(number):
    """

    :param number: Positive integer
    :type number: int
    :return: Final digit of repetitive calculation of digit sum
    :rtype: int
    """
    if number <= 9:
        return number
    number = calculate_digit_sum(number)
    return multiple_digit_sum_recursive(number)


# Aufgabe 4

def convert_raw_data(source, destination):
    """
    die Funktion wendet calculate_digit_sum auf
    die Daten einer .csv Datei an.

    :param source: Datenquelle
    :param destination: wo muss das Ergebnis gespeichert sein
    :return:
    """
    with open(f'{source}') as quelle, open(f'{destination}', 'w') as ergebnis:
        readed_daten = quelle.read().split('\n')
        for i in readed_daten:
            zwei_zeilen = i.split(',')
            digit_sum1 = calculate_digit_sum(zwei_zeilen[0])
            digit_sum2 = calculate_digit_sum(zwei_zeilen[1])
            ergebnis.write(f"{digit_sum1},{digit_sum2}\n")


# Testaufrufe

if __name__ == "__main__":
    print(calculate_digit_sum(5237))
    print(calculate_digit_sum(-5237))
    print(multiple_digit_sum_iterative(5237))
    print(multiple_digit_sum_recursive(5237))
    convert_raw_data("raw_data.csv", "digit_sums.csv")
