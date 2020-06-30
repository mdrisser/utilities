"""
This file contains various conversion functions for use within Python programs.
Conversions:
Computer - various computer formats
Temperature - Various temperature formats
Length - metric to/from imperial
"""


#####
## COMPUTER CONVERSIONS
def bytes_to_human(bytes, suffix="B"):
    """
    Original Code:
    Scale bytes to its proper, human readable format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


#####
## TEMPERATURE CONVERSIONS
def c_to_f(degrees):
    """
    Convert degrees celcius to degrees fahrenheit
    """
    return degrees * 9/5 + 32


def c_to_k(degrees):
    """
    Convert degrees celcius to degrees kelvin
    """
    return degrees + 273.15


def f_to_c(degrees):
    """
    Convert degrees fahrenheit to degrees celcius
    """
    return (degrees - 32) * 5/9


def f_to_k(degrees):
    """
    Convert degrees fahrenheit to degrees kelvin
    """
    return (degrees + 459.67) * 5/9


def k_to_c(degrees):
    """
    Convert degrees kelvin to degrees celcius
    """
    return degrees - 273.15


def k_to_f(degrees):
    """
    Convert degrees kelvin to degrees fahrenheit
    """
    return degrees * 9/5 - 459.67


#####
## LENGTH CONVERSIONS
def mm_to_in(mm):
    """
    Convert millimeters to inches
    """
    return mm / 25.4


def cm_to_in(mm):
    """
    Convert centimeters to inches
    """
    return mm / 2.54


def m_to_f(meters):
    """
    Convert meters to feet
    """
    return meters / 0.3048


def in_to_mm(inches):
    """
    Convert inches to millimeters
    """
    return inches * 25.4


def in_to_cm(inches):
    """
    Convert inches to centimeters
    """
    return inches * 2.54


def f_to_m(feet):
    """
    Convert feet to meters
    """
    return feet * 0.3048
