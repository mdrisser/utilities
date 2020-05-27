"""
The degree sign, useful for displaying temperatures
"""
deg_sign = u'\N{DEGREE SIGN}'


def esc(code):
    """
    Performs an escape on <code>
    """
    return f'\033[{code}m'
