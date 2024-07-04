import unittest
import hi

class TestCalc(unittest.TestCase):
    """
    Test the add function from the calc library
    """
    hi.hello()
    def test_add_integers(self):
        """
        Test that the addition of two integers returns the correct total
        """

        

if __name__ == '__main__':
    unittest.main()
