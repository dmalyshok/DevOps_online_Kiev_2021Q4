import unittest
import solv_square_equation
'''
-discriminant(a, b, c) 
-roots(d, a, b, c) 
-solv_square(a, b, c) -> roots   
''' 
class EquationTest(unittest.TestCase):
     def test_dis(self):
        self.assertEqual(solv_square_equation.discriminant(1, 2, 3), -8)
        
     def test_root(self):
         self.assertEqual(solv_square_equation.roots(196, 1, -26, 120), 'd > 0')
         self.assertEqual(solv_square_equation.roots(0, 1, 6, 9), 'd == 0')
         self.assertEqual(solv_square_equation.roots(-64, 1, 2, 17), 'd < 0')

     def test_solv(self):
         self.assertEqual(solv_square_equation.solv_square(1, -26, 120), (20.0,6.0))
        
        
if __name__ == '__main__':
    unittest.main()