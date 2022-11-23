from pytest import *

from account import *


class Test:

    def setup_method(self):
        self.test_account = Account('Marry')

    def teardown_method(self):
        del self.test_account


    def test_init(self):
        assert self.test_account.get_name() == 'Marry'
        assert self.test_account.get_balance() == 0

    def test_deposit(self):
        assert self.test_account.deposit(6.2) is True
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)

        assert self.test_account.deposit(0) is False
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)

        assert self.test_account.deposit(-6) is False
        assert self.test_account.get_balance() == approx(6.2, abs=0.001)

    def test_withdraw(self):

        self.test_account.deposit(6.2)
        assert self.test_account.withdraw(3) is True
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)
        assert self.test_account.withdraw(0) is False
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)

        assert self.test_account.withdraw(-6) is False
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)

        assert self.test_account.withdraw(5) is False
        assert self.test_account.get_balance() == approx(3.2, abs=0.001)
