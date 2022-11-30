#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        1_digit = number % 10
    else:
        1_digit = number % -10
        1_digit *= -1

    print("{:d}".format(1_digit), end='')
    return (1_digit)
