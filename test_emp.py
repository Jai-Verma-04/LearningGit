import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("SETUP")
    

    @classmethod
    def tearDownClass(cls) -> None:
        print("TEARDOWN")
    

    def setUp(self):
        print('setup')
        self.emp1 = Employee("Jai", "Verma", 50000)
        self.emp2 = Employee("Himanshu", "Negi", 60000)

    
    def tearDown(self):
        print('tear down')


    def test_apply_raise(self):
        print('test_apply_raise')        
        self.emp1.apply_raise()
        self.emp2.apply_raise()

        self.assertEqual(self.emp1.pay, 52500)
        self.assertEqual(self.emp2.pay, 63000)


    def test_fullname(self):
        print('test_fullname')
        self.assertEqual(self.emp1.fullname, "Jai Verma")
        self.assertEqual(self.emp2.fullname, "Himanshu Negi")
        

if __name__ == '__main__':
    unittest.main()