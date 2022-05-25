"""An interactive random demo auction.
Run this on the console and place your own bids.
"""
from auction import Auction
import random
import time


def demo_auction():
    """Run a random auction.  Stop after max_bids bidsa"""
    import random
    # number of bids to accept
    max_bids = 12
    bidders = ["Prayut Chanocha", "Taksin Shinowat",
               "Donald Trump", "Barrack Obama"]
    auction = Auction("Vacation to Ko Samui", 100)
    print(">>> auction =", auction.__repr__())
    print(">>> auction.start()")
    auction.start()
    pause("Press ENTER to start bidding...")
    nextbidder = 0
    amount = 0
    for n in range(0, max_bids):
        if n % 4 == 3:
            bidder = "You"
            print(">>> auction.best_bid()")
            print(auction.best_bid())
            bid = input("\nYour turn.  How much do you bid? ")
            try:
                amount = float(bid)
                if amount == int(amount):
                    amount = int(amount)
            except Exception:
                amount = auction.best_bid() + 1
                print(f"{bid} is not a valid number. You bid {amount}.")
        else:
            # random bidder
            bestbidder = auction.winner()
            try:
                lastbidder = bidders.index(bestbidder)
            except ValueError:
                lastbidder = 0
            nextbidder = (lastbidder + random.randint(1,
                          len(bidders)-1)) % len(bidders)
            bidder = bidders[nextbidder]
            amount = make_random_bid(auction)
        print_and_bid(auction, bidder, amount)

    print(">>> auction.stop()")
    auction.stop()
    print()
    pause("The bidding is over! Press ENTER to see who won... ")
    print()
    print(">>> auction.winner()")
    print(auction.winner())
    print(">>> auction.best_bid()")
    print(auction.best_bid())


def make_random_bid(auction) -> float:
    bestbid = auction.best_bid()
    increment = auction.min_increment
    # return a valid bid most of the time
    # first bid should always be valid
    if bestbid == 0:
        amount = int(increment + 10)
    elif random.randint(1, 6) > 1:
        amount = int(bestbid + increment*random.randint(2, 5)//2 + 10)
    else:
        # bid too low
        amount = int(bestbid + increment//2)
    return amount


def print_and_bid(auction, bidder, amount):
    print(f'>>> auction.bid("{bidder}", {amount})')
    # wait for ENTER
    # pause()
    try:
        auction.bid(bidder, amount)
    except Exception as e:
        ex_name = type(e).__name__
        print(f'{ex_name}:', e)
    time.sleep(1)  # 1 second


def pause(prompt=""):
    """Wait for user to press ENTER."""
    reply = input(prompt)
    return


if __name__ == "__main__":
    demo_auction()
