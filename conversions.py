class BinaryError(Exception):
    pass


class HexError(Exception):
    pass


def bin_to_dec(binary):
    """ Receives a binary integer and returns the decimal value. """

    integer = 0
    two_power = len(binary) - 1
    try:
        for i in range(len(binary)):
            if binary[i] not in "01":
                raise BinaryError
            integer += int(binary[i]) * (2 ** two_power)
            two_power -= 1
        return integer
    except BinaryError:
        return "Enter Valid Binary"


def dec_to_bin(decimal):
    """ Receives a decimal integer and returns a string representing the integer in binary. """

    binary = ""
    try:
        decimal = int(decimal)
        while decimal > 0:
            if decimal % 2 == 0:
                binary += "0"
            else:
                binary += "1"
            decimal = decimal // 2
        return binary[::-1]
    except ValueError:
        return "Enter Valid Integer"


def hex_to_dec(hex_number):
    """ Receives a hexadecimal integer and returns the decimal value. """

    hex_values = {"A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    integer = 0
    sixteen_power = len(hex_number) - 1

    try:
        for i in range(len(hex_number)):
            if hex_number[i].upper() not in "ABCDEF012345678910":
                raise HexError
            if hex_number[i] in hex_values:
                integer += hex_values[hex_number[i]] * (16 ** sixteen_power)
            else:
                integer += int(hex_number[i]) * (16 ** sixteen_power)
            sixteen_power -= 1
        return integer
    except HexError:
        return "Enter Valid Hex"


def dec_to_hex(decimal_number):
    """ Receives a decimal integer and returns a string representing the integer in hexadecimal. """

    dec_values = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}

    hex_number = ""
    try:
        decimal_number = int(decimal_number)
        while decimal_number > 0:
            remainder = decimal_number % 16
            if remainder in dec_values:
                hex_number += dec_values[remainder]
            else:
                hex_number += str(remainder)
            decimal_number = decimal_number // 16

        return hex_number[::-1]
    except ValueError:
        return "Enter Valid Integer"


def bin_to_hex(binary):
    """ Receives a binary integer and returns the hexadecimal value. """

    decimal = bin_to_dec(binary)
    if isinstance(decimal, int):
        hex_number = dec_to_hex(decimal)
        return hex_number
    else:
        return decimal


def hex_to_bin(hex_number):
    """ Receives a hexadecimal integer and returns the binary value. """

    decimal = hex_to_dec(hex_number)
    if isinstance(decimal, int):
        binary_number = dec_to_bin(decimal)
        return binary_number
    else:
        return decimal
