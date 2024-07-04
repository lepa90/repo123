import unittest
import hi
class TestBankOperations(unittest.TestCase):
    def test_insufficient_deposit(self):
      # Arrange
      a = hi.BankAccount(1)
      a.deposit(100)
      # Act
      outcome = a.withdraw(200)
      # Assert
      self.assertFalse(outcome)

if __name__ == '__main__':
    unittest.main()