import unittest
import main

# DO NOT TOUCH THE BELOW CODE

class Test_1(unittest.TestCase):
  def test_01(self):
    self.assertEqual(main.highest_of(5,4), 5)

  def test_02(self):
    self.assertEqual(main.highest_of(6,94), 94)
    
if __name__ == '__main__':
  unittest.main(verbosity=2)
    
