"""Tests of the Auction class.

Author: Preawpan Thamapipol
"""
import unittest

from auction import Auction, AuctionError


class TestAuction(unittest.TestCase):
    """Tests of the Auction class."""

    def setUp(self):
        """Set up an auction before each test."""
        # you can still create an auction inside a test
        # if you want special values
        self.auction = Auction("test auction", min_increment=2)

    def test_init(self):
        """Test Auction initialization."""
        # test that Auction is initialized correctly
        self.assertEqual(self.auction.name, "test auction")
        self.assertEqual(self.auction.best_bid(), 0)
        self.assertEqual(self.auction.increment, 2)
        self.assertFalse(self.auction.is_active())

    def test_start(self):
        """Test starting an auction."""
        self.auction.start()
        self.assertTrue(self.auction.is_active())

    def test_bid_when_not_active(self):
        """Bid when not active is not allow"""
        self.auction.start()
        self.auction.bid('Tw', 10 + self.auction.min_increment)
        self.auction.stop()
        with self.assertRaises(AuctionError):
            self.auction.bid("bob", 15)

    def test_empty_name_bit(self):
        """Bid must have a name"""
        name_list = ["", "     "]
        self.auction.start()
        for name in name_list:
            with self.assertRaises(AuctionError):
                self.auction.bid(name, 15 + self.auction.min_increment)

    def test_non_string_name_type_bid(self):
        """name of bid must be string"""

        lst_num = [5, 10.5]
        self.auction.start()
        for name in lst_num:
            with self.assertRaises(TypeError):
                self.auction.bid(name, 15 + self.auction.min_increment)

    def test_non_positive_amount_and_float_bid(self):
        """cant bid with negative or zero amount"""

        self.auction.start()
        all_money = [0, -15]
        self.auction.bid('Tw', 10.5 + self.auction.min_increment)
        for amount in all_money:
            with self.assertRaises(AuctionError):
                self.auction.bid("bob", amount)

    def test_non_integer_bid(self):
        """bid must be number"""

        self.auction.start()
        self.auction.bid('Tw', 10 + self.auction.min_increment)
        with self.assertRaises(TypeError):
            self.auction.bid("bob", "15")

    def test_bid_too_low(self):
        """bid must be higher than previous bid"""

        self.auction.start()
        self.auction.bid('bob', 15 + self.auction.min_increment)
        with self.assertRaises(AuctionError):
            self.auction.bid('james', 10)

    def test_bid_not_in_threshold(self):
        """bid must be the best bid plus minimum bid"""

        self.auction.start()
        increment = self.auction.min_increment
        self.auction.bid('bob', 15 + increment)
        self.auction.bid('Tw', self.auction.best_bid() + increment)
        with self.assertRaises(AuctionError):
            self.auction.bid('God', self.auction.best_bid() + increment - 1)

    def test_bid_winner(self):
        """test winner of the bid"""

        bidder_dct = {'bob': 15, 'God': 20, 'god': 25, 'Tonwan': 30}

        self.auction.start()
        for name, amount in bidder_dct.items():
            self.auction.bid(name, amount + self.auction.min_increment)

        self.assertEqual(self.auction.winner(), 'Tonwan')

    def test_random_bid_and_test_winner(self):
        """bid amount less than now best bid then check winner"""
        self.auction.start()
        self.auction.bid('God', 15 + self.auction.min_increment)
        with self.assertRaises(AuctionError):
            self.auction.bid('Jim', 10)

        self.assertEqual(self.auction.winner(), 'God')

    def test_active_or_inactive_bid(self):
        """winner or best_bidder function must be call any time
        even auction is active"""

        increment = self.auction.min_increment
        first_bidder = {'bob': 15, 'james': 20}
        second_bidder = {'god': 25, 'Tonwan': 30}

        self.auction.start()
        for name, amount in first_bidder.items():
            self.auction.bid(name, amount + increment)
        # test while bid is active
        self.assertEqual(self.auction.winner(), 'James')
        self.assertEqual(self.auction.best_bid(), 20 + increment)

        for name, amount in second_bidder.items():
            self.auction.bid(name, amount + increment)
        # twst while bid is inactive
        self.auction.stop()

        self.assertEqual(self.auction.winner(), 'Tonwan')
        self.assertEqual(self.auction.best_bid(), 30 + increment)

    def test_bruh_name(self):
        """the name must be change to normal format after bid"""

        name_dct = ['PrEawPan     thAmApipol', 'ThiTiRat          tONwaN']
        increment = 0
        self.auction.start()
        for name in name_dct:
            self.auction.bid(name, 15 + increment)
            increment += self.auction.min_increment + 1

        self.assertEqual(self.auction.winner(), 'Thitirat Tonwan')
