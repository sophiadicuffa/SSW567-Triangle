"""Module providing a function testing if user input is a triangle"""

def classify_triangle(a, b, c):

    """Function testing if user input is a triangle."""

    if not (isinstance(a, int) and isinstance(b, int) and isinstance(c, int)):
        return 'InvalidInput'
    # require that the input values be >= 0 and <= 200
    if (a >= 200 or b >= 200 or c >= 200 or a <= 0 or b <= 0 or c <= 0):
        return 'InvalidInput'
    if (a >= (b + c)) or (b >= (a + c)) or (c >= (a + b)):
        return 'NotATriangle'

    if a == b and b == c:
        return 'Equilateral'
    elif (a ** 2) + (b ** 2) == c ** 2 or (b ** 2) + (c ** 2) == a ** 2 or (a ** 2) + (c ** 2) == b ** 2:
        return 'Right'
    elif a != b and b != c and a != c:
        return 'Scalene'
    else:
        return 'Isosceles'
