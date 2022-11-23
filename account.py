class Account:
    """
    A class representing details for account's object
    """

    def __init__(self, name: str) -> None:

        """
        Constructor to create initial name of a person object.
        :param account_name: a person's name.
        :param account_balance: a person's initial balance
        """

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self, amount: float) -> bool:
        """
        :param amount: the amount in the account
        :return: return true if any amount added to the amount, otherwise return false
        """

        if amount > 0:
            self.__account_balance += amount
            return True
        else:
            return False

    def withdraw(self, amount: float) -> bool:
        """

        :param amount: the amount in the account
        :return: return true if any amount withdrawn to the initial amount, otherwise return false
        """

        if amount <= 0 or amount > self.__account_balance:
            return False

        else:
            self.__account_balance -= amount
            return True

    def get_balance(self) -> float:
        """
            Method to access the account balance.
            :return: the initial account's balance
            """

        return self.__account_balance

    def get_name(self) -> str:
        """
            Method to access the account name.
            :return: the initial account's name
            """

        return self.__account_name
