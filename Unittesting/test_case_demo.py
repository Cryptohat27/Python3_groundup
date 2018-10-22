"""

"""

import unittest
 
class TestCaseDemo(unittest.TestCase):

    def setup(self):
        print("I will run once before every test")
        
    def test_methodA(self):
        print("running method A")

    def test_method(self):
        print("running method B")
    
    def tearDown(self):
        print("I will run after every test")
                
if __name__ == '__main__':
    unittest.main(verbosity=2)
