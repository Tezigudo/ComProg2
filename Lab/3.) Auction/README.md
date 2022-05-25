## Auction Testing Problem

Write unit tests for the Auction class. Write your tests in `test_auction.py`.

- Write tests for each of the Auction requirements.
- Write tests for how the Auction code **should** behave based on the **specification**. 
- Do not test for how the sample Auction code **actually** hehaves. The code may contain defects!
- Test behavior, not attributes. The implementation & attributes may change.


## Running Your Tests

When you push code to Github, a Github Action will automatically run your tests,
using **8 different versions** of the Auction code.

Click the **Action** tab on Github to view the results.

Auction Version 1: Auction is correct. Your tests should **all pass**.

Auction Version 2-8: At least 1 defect. Some of your tests should **fail** or **error**.


## What to Submit

Complete the Error Analysis section below in this README.md.

Push your `test_auction.py` and README.md to Github classroom.


## Error Analysis

Study the output of Github Actions.  **Do not** try to look at the source code.  The goal is to identify the defect based on your tests.

- Write the name of your test(s) that fail. To avoid underscore being interpretted as a formatting command, write the test name in backquotes (`test_constructor`).
- Briefly describe the defect, such as "bids are accepted while the auction is stopped".
- If your answer is too long to fit in the table, write a paragraph below & identify which Auction Version you are writing about.

### note all of the below problem I have fixed

| Auction Version | Failing Test | Your analysis of defect                     |
|---------|--------------|:----------------------------------------------------|
| 1       | All PASSED | |
| 2       |`test_bid_not_in_threshold`| bid must higher than previous bid|
| 3       |`test_bid_not_in_threshold` | `AuctionError` is raised due to current bid is equal to bestbid + minimum incremnt it will raise|
| 4       | `test_bid_when_not_active`|`AuctionError` is raised due tt bid while Auction isn't active|
| 5       |`test_bid_not_in_threshold`, `test_bid_too_low` , `test_non_positive_amount_and_float_bid`, and `test_random_bid_and_test_winner`| `AuctionError` is caused by many reason such as first bid must higher that previous bid and more than best bid plus threshold(min increment of each bid), then it bid with **zero** or **negative** amount, the last one is seem like winner is not valid I guess that testcase is calculate winner by last bidder instead of bidder **who have bidded most money**|
| 6       |`test_init`| Seem like at the initialize of object it is set active status to **True** instead of **False**|
| 7       | `test_non_positive_amount_and_float_bid`|in this case `TypeError` was raised due amount of bid is float but it can be float or any integer and doesn't need to raise anyError|
| 8       | `test_empty_name_bit`, `test_random_bid_and_test_winner`|  `uctionError` not raised because on the bid function doesnt check the white space or empty name, Then the code doesnt check bid winner by usting max manoy bidder but i think code used lastest bid instead of former|
