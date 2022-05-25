import unittest
from wallet import Wallet
from cash import Coin, Banknote

class WalletTest(unittest.TestCase):

    def test_wallet_constructor(self):
        """A new Wallet should be empty."""
        wallet = Wallet()
        self.assertTrue(wallet.is_empty())
        self.assertEqual(0, len(wallet.get_items()))

    def test_deposit(self):
        """Can deposit a single item."""
        coin = Coin(5, "Baht")
        wallet = Wallet()
        wallet.deposit(coin)
        self.assertFalse(wallet.is_empty())
        items = wallet.get_items()
        self.assertListEqual([coin], items)