import unittest

# Die zu testende Funktion
def add_numbers(a, b):
    return a + b

# Die Testklasse für Regressionstests
class TestAdditionFunction(unittest.TestCase):

    # Test für die korrekte Addition von zwei positiven Zahlen
    def test_add_positive_numbers(self):
        result = add_numbers(5, 10)
        self.assertEqual(result, 15)

    # Test für die korrekte Addition von zwei negativen Zahlen
    def test_add_negative_numbers(self):
        result = add_numbers(-3, -7)
        self.assertEqual(result, -10)

    # Test für die korrekte Addition von positiver und negativer Zahl
    def test_add_mixed_numbers(self):
        result = add_numbers(8, -4)
        self.assertEqual(result, 4)

    # Test für die korrekte Addition von Nullen
    def test_add_zeros(self):
        result = add_numbers(0, 0)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    # Führe die Tests aus
    unittest.main()
