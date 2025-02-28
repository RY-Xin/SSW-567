import unittest
from classify_triangle import classify_triangle

class TestClassifyTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(2, 2, 2), "Equilateral Triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(2, 2, 3), "Isosceles Triangle")
        self.assertEqual(classify_triangle(3, 2, 2), "Isosceles Triangle")
        self.assertEqual(classify_triangle(2, 3, 2), "Isosceles Triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(7, 10, 5), "Scalene Triangle")

    def test_right_triangle(self):
        self.assertEqual(classify_triangle(3, 4, 5), "Scalene Triangle and Right")
        self.assertEqual(classify_triangle(5, 12, 13), "Scalene Triangle and Right")
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene Triangle and Right")

    def test_invalid_triangle(self):
        self.assertEqual(classify_triangle(1, 2, 3), "Invalid Triangle")
        self.assertEqual(classify_triangle(5, 1, 1), "Invalid Triangle")

    def test_invalid_input(self):
        self.assertEqual(classify_triangle(-1, 2, 3), "Invalid Triangle")
        self.assertEqual(classify_triangle(0, 2, 3), "Invalid Triangle")
        self.assertEqual(classify_triangle(1, 1, 3), "Invalid Triangle")
        
    def test_scalene_and_right_edge_case(self):
        self.assertEqual(classify_triangle(6, 8, 10), "Scalene Triangle and Right")

    def test_equilateral_large(self):
        self.assertEqual(classify_triangle(99999, 99999, 99999), "Equilateral Triangle")

    def test_negative_edges(self):
        self.assertEqual(classify_triangle(-5, -5, -5), "Invalid Triangle")

    def test_zero_edges(self):
        self.assertEqual(classify_triangle(0, 5, 5), "Invalid Triangle")

if __name__ == "__main__":
    unittest.main(exit=False)
