import unittest
max_integer = __import__("6-max_integer").max_integer

class TestMax(unittest.TestCase):
    def test_max(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertRaises(TypeError, max_integer, ["a", "b", 8])
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([-2, -6, -1]), -1)
        self.assertEqual(max_integer([3, 4.5, 2]), 4.5)
        self.assertRaises(TypeError, max_integer, 7)
        self.assertEqual(max_integer([8]), 8)
        self.assertEqual(max_integer([9, 9, 9, 9]), 9)
        self.assertEqual(max_integer(["hi", "hello"]), "hi")
        self.assertRaises(TypeError, max_integer, None)
if __name__ == "__main__":
    unittest.main()
