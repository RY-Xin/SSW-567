"""
This module contains a function to classify triangles based on side lengths.
"""
def classify_triangle(a, b, c):
    """
    Classifies a triangle based on its side lengths.

    Args:
        a (float): Length of the first side.
        b (float): Length of the second side.
        c (float): Length of the third side.

    Returns:
        str: Type of the triangle (e.g., "Equilateral", "Isosceles", "Scalene", "Not a triangle").
    """

    sides = sorted([a, b, c])
    a, b, c = sides

    if a + b <= c:
        return "Invalid Triangle"

    is_right = a**2 + b**2 == c**2

    if a == b == c:
        return "Equilateral Triangle"

    if b in (a, c):
        return "Isosceles Triangle and Right" if is_right else "Isosceles Triangle"

    return "Scalene Triangle and Right" if is_right else "Scalene Triangle"
