"""This module provides Auction and AuctionError."""
import re


class Auction:
    """An auction where people can submit bids for an item.

    One Auction instance is for bidding on a single item.
    """

    def __init__(self, auction_name: str, min_increment: float = 1):
        """Create a new auction with given auction name.

           :param auction_name: a string name for this Auction
           :param min_increment: is the minimum amount that a new bid
               must exceed the current best bid. Default is 1.
        """
        self.name = auction_name
        self.bids = {"no bids": 0}
        self.increment = min_increment
        self._active = False

    def start(self):
        """Enable bidding."""
        self._active = True

    def stop(self):
        """Disable bidding."""
        self._active = False

    @property
    def min_increment(self):
        """Get the minimum required increment for bids.

        Each new bid must be higher than the previous bid by at
        least this amount (min_increment).
        """
        return self.increment

    def is_active(self) -> bool:
        """Query if bidding is enabled. Returns True if bidding enabled."""
        return self._active

    def bid(self, bidder_name: str, amount: float):
        """Submit a bid to this auction.

        :param bidder_name:  name of bidder, a non-empty non-blank string.
               Names are converted to Title Case, and excess space
               inside and surrounding the string is removed.
               "harry   haCkeR " is normalized to "Harry Hacker"
        :param amount:  amount (int or float) of this bid.
               Must be positive and greater than previous best bid by at
               least the min_increment (property), which is set in the
               constructor and has a default value of 1.

        Raises:
            TypeError if bidder_name or amount are incorrect data types.
            AuctionError if bidder_name is only whitespace.
            AuctionError if bidding is disabled or bid amount is too low.
        """
        if not isinstance(bidder_name, str):
            raise TypeError("Bidder name must be a non-empty string")
        if not isinstance(amount, (int, float)):
            raise TypeError('Amount must be a number')
        if not self._active:
            raise AuctionError('Bidding not allowed now')
        if len(bidder_name) < 1:
            raise AuctionError("Missing bidder name")
        if amount < 0:
            raise AuctionError('Amount is invalid')
        # check if this is best bid so far
        if amount <= self.best_bid() + self.increment:
            raise AuctionError("Bid is too low")
        # fix case of letters and remove whitespace
        bidder_name = Auction.normalize(bidder_name)
        # Accept the bid!
        self.bids[bidder_name] = amount

    def best_bid(self):
        """Return the highest bid so far."""
        return max(self.bids.values())

    def winner(self):
        """Return name of person who placed the highest bid."""
        best = self.best_bid()
        for (bidder, bid) in self.bids.items():
            if bid == best:
                return bidder

    def __str__(self):
        """Return a string description for this auction."""
        return 'Auction for '+self.name

    def __repr__(self):
        """String form of command to recreate the Auction."""
        if self.increment == 1:
            return f"Auction('{self.name}')"
        return f"Auction('{self.name}', min_increment={self.increment})"

    @classmethod
    def normalize(cls, name):
        """
        Convert a name to title case and remove excess whitespace.

        Examples:
        >>> Auction.normalize("KUNG FU  ")
        'Kung Fu'
        >>> Auction.normalize("KUNG-FU  ")
        'Kung-Fu'
        >>> Auction.normalize("   too    MuCh  SpacE")
        'Too Much Space'
        >>> Auction.normalize("noSpacE")
        'Nospace'
        >>> Auction.normalize("    ")
        ''
        """
        namewords = re.split("\\s+", name.strip())
        name = " ".join(namewords)
        return name.title()


class AuctionError(Exception):
    """
    Exception to throw when an invalid Auction action is performed.
    """
    # Superclass provides all the behavior we need, so nothing to add here.
