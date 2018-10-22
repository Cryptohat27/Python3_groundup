"""

"""

import unittest
 
class TestCaseDemo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("#" * 30)
        print("I will run once before all the test")
        print("#" * 30)


    def setup(self):
        print("I will run once before every test")
        
    def test_methodA(self):
        print("running method A")

    def test_method(self):
        print("running method B")
    
    def tearDown(self):
        print("I will run after every test")
    
    def tearDownClass(cls):
        print("#" * 30)
        print(" I will run only once after all test")
        print("#" * 30)

if __name__ == '__main__':
    unittest.main(verbosity=2)
