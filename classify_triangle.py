def classify_triangle(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides

    if a + b <= c:  
        return "Invalid Triangle"

    is_right = a**2 + b**2 == c**2

    if a == b == c:
        return "Equilateral Triangle"

    if a == b or b == c:
        return "Isosceles Triangle and Right" if is_right else "Isosceles Triangle"

    return "Scalene Triangle and Right" if is_right else "Scalene Triangle"
