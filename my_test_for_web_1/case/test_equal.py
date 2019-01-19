import unittest


class CeShiEqual(unittest.TestCase):
    def test01(self):
        self.a = 3
        self.b = 3
        self.assertTrue(self.a == self.b)


if __name__ == '__main__':
    unittest.main()