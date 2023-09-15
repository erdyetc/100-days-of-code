import os
import art_auction

more_bidders = True
bids = {}

def find_highest_bid(bids_list):
    max_value_bidders = []
    max_value = max(bids_list.values())
    for key in bids_list:
        if bids_list[key] == max_value:
            max_value_bidders.append(key)
    max_value = "{:.2f}".format(max_value)
    print(f"The winner(s) is/are {' and '.join(max_value_bidders)} with a bid of ${max_value}")

while more_bidders == True:
    os.system('clear')
    print(art_auction.logo)
    name = input("What is your name? ")
    bid = float(input("What is your bid? $"))
    bids[name] = bid
    more_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
    if not more_bid == "no" and not more_bid == "yes":
        print("That was not a valid response.")
        more_bid = input("Are there any other bidders? Type 'yes' or 'no'. ").lower()
        if more_bid == "no":
            more_bidders = False
            find_highest_bid(bids)
    elif more_bid == "no":
        more_bidders = False
        find_highest_bid(bids)
    
"""100 days of code solution

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = bidding_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
"""
