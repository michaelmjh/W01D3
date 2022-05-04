def return_10():
    return 10


def add(number_1, number_2):
    return number_1 + number_2


def multiply(number_1, Number_2):
    return number_1 * Number_2


def length_of_string(test_string):
    return len(test_string)


def add_string_as_number(number_1, number_2):
    return int(number_1) + int(number_2)


def number_to_short_month_name(number):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    return months[number - 1]


def reverse_word(word):
    return word[::-1]


def convert_temp(number):
    calc = (number - 32) * (5/9)
    return calc