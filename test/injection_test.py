import injection, croissant
import unittest

class TestInjection(unittest.TestCase):
    def test_tri_insertion(self):
        tab = [9, 5 , 7 , 3 , 1 , 2 , 4 , 6 , 8 , 0 , 50 , 5]
        result = [0 , 1 , 2 , 3 , 4 , 5 , 5 , 6 , 7 , 8 , 9 , 50]
        self.assertEqual(injection.tri_Insersiton(tab), result)

    def test_tri_insertion_random(self):
        tab = croissant.generate_tab(100)
        result = croissant.ordre_croissant(tab)
        print(tab)
        print(result)
        self.assertEqual(injection.tri_Insersiton(tab), result)

if __name__ == '__main__':
    unittest.main()