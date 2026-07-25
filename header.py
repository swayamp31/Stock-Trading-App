# Stock Trading App
# this is header.py file 
# Author: Swayam Patel
# in this file , here I layout my app. this is how it looks like.

def print_header():
    print("=== Stock Trading App ===")

# this will run start of the code everysingle time.
def print_menu():
    print("\n1. View Portfolio")
    print("2. Buy Stock")
    print("3. Sell Stock")
    print("4. historical data")
    print("5. Quit")


def display_portfolio(portfolio):
    print("\n=== Portfolio ===")
    for stock, quantity in portfolio.items():
        print(f"{stock}: {quantity} shares")
    print("=================")
