import unittest
from bankAccount import BankAccount

class TestBankAccount(unittest.TestCase):
    def setUp(self):
        """Create a bank account for testing with an initial balance of 1000."""
        self.account = BankAccount("Alice", 1000)

    def test_initial_balance(self):
        """Test if the initial balance is set correctly."""
        self.assertEqual(self.account.get_balance(), 1000)

    def test_deposit(self):
        """Test if deposit function adds money correctly."""
        self.account.deposit(500)
        self.assertEqual(self.account.get_balance(), 1500)

    def test_withdraw(self):
        """Test if withdraw function deducts money correctly."""
        self.account.withdraw(300)
        self.assertEqual(self.account.get_balance(), 700)

    def test_withdraw_insufficient_funds(self):
        """Test that withdrawing more than available balance raises an error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_negative_deposit(self):
        """Test that depositing a negative amount raises an error."""
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_negative_withdrawal(self):
        """Test that withdrawing a negative amount raises an error."""
        with self.assertRaises(ValueError):
            self.account.withdraw(-50)

    def test_zero_deposit(self):
        """Test that depositing zero raises an error."""
        with self.assertRaises(ValueError):
            self.account.deposit(0)

    def test_withdraw_full_balance(self):
        """Test that withdrawing the exact balance leaves zero balance."""
        self.account.withdraw(1000)
        self.assertEqual(self.account.get_balance(), 0)

    def test_multiple_transactions(self):
        """Test multiple deposits and withdrawals in a sequence."""
        self.account.deposit(200)
        self.account.withdraw(100)
        self.account.deposit(300)
        self.assertEqual(self.account.get_balance(), 1400)

if __name__ == '__main__':
    unittest.main()
