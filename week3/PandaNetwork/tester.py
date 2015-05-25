import unittest
from bank_account import BankAccount


class BankAccountTest(unittest.TestCase):

    def setUp(self):
        self.acc = BankAccount("da", 10, "$")
        self.acc2 = BankAccount("ne", 20, "$")

    def test_constructor(self):
        self.assertTrue(isinstance(self.acc, BankAccount))

    def test_int_case(self):
        self.assertEqual(int(self.acc), 10)

    def test_input_values(self):
        with self.assertRaises(ValueError):
            acc = BankAccount("da", -10, "&")

    def test_amount(self):
        self.assertTrue(self.acc.deposit(10))

    def test_deposit_input_value(self):
        with self.assertRaises(ValueError):
            self.acc.deposit(-10)

    def test_deposit_changes_the_value(self):
        self.acc.deposit(20)
        self.assertEqual(int(self.acc), 30)

    def test_current_ballance(self):
        self.assertEqual(self.acc.ballance(), 10)

    def test_withdraw_exists(self):
        self.assertTrue(self.acc.withdraw(10))

    def test_withdraw_works(self):
        self.assertTrue(self.acc.withdraw(10))

    def test_str_exists(self):
        self.assertEqual(str(self.acc),
                         "Bank account for da with balance of 10$")

    def test_wrong_type_deposit(self):
        with self.assertRaises(TypeError):
            self.acc.deposit("dada")

    def test_right_type_deposit(self):
        self.assertTrue(self.acc.deposit(50))

    def test_wrong_type_withdraw(self):
        with self.assertRaises(TypeError):
            self.acc.withdraw("da")

    def test_currency(self):
        self.assertEqual(self.acc.currency(), "$")

    def test_account_true_transfer_to(self):
        self.assertFalse(self.acc.transfer_to(self.acc, 20))

    def test_same_currencies(self):
        acc1 = BankAccount("are", 10, "&")
        self.assertFalse(self.acc.transfer_to(acc1, 5))

    def test_setter_ballance(self):
        self.acc.incr_ballance(10)
        self.assertEqual(self.acc.ballance(), 20)

    def test_transfer_to_working_receiver(self):
        self.acc.transfer_to(self.acc2, 5)
        self.assertEqual(self.acc2.ballance(), 25)

    def test_transfer_to_working_sender(self):
        self.acc.transfer_to(self.acc2, 5)
        self.assertEqual(self.acc.ballance(), 5)
if __name__ == '__main__':
    unittest.main()
