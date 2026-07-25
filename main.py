# Stock Trading App
#Main file that will communicate directly with the user and pose a few questions.
# Author: Swayam Patel

#To import all files and use matplotlib if user wants to make a plot out of the historical data.
#Print_header, print_menu, and display-portfolio.
from stocks import buy_stock, sell_stock, view_portfolio, get_historical_stock_prices, save_portfolio, load_portfolio
import view_portfolio, buy_stock, sell_stock, get_historical_stock_prices, save_portfolio, load_portfolio
import matplotlib.pyplot as plt

def main():
#Portfolio will always load automatically and therefore, they won’t lose any of their data each time that they run the code.
portfolio = load_portfolio()

#calling the Layout from header.py 
print_header()

#User can log off and later go back in.
while True:
print_menu()

choice = input("Enter your choice (1-5): ")

if choice == "1":
display_portfolio(view_portfolio(portfolio))
elif choice == "2":
stock = input("Enter the stock name: ")
quantity = int(input("Enter the quantity to buy: "))
buy_stock(portfolio, stock, quantity)
elif choice == "3":
stock = input("Enter the stock name: ")
quantity = int(input("Enter the quantity to sell: "))
sell_stock(portfolio, stock, quantity)
elif choice == "4":
stock = input("Enter the stock name: ")
days = int(input("Enter the number of days for historical data: "))
historical_prices = get_historical_stock_prices(stock, days)
if historical_prices is not None:
print("\n=== Market Prices of {stock} during 1980—2015”)
print(historical_prices)

plot_choice = input("Do you want to plot the historical data? (y/n): ")
if plot_choice.lower() == 'y':
plot_stock_prices(historical_prices, stock)
elif choice == "5":
save_portfolio(portfolio)
print(“Leaving the stock trading app…bye!”)
break
else:
print(“Choose invalid. Choose a number from 1-5”).

#This method displays the results in a graph form.
def plot_stock_prices(historical_prices, stock):
plt.plot(historical_prices.index, historical_prices.values)
plt.title(f"Historical Stock Prices for {stock}")
plt.xlabel("Date")
plt.ylabel("Closing Price")
plt.show()
plt.switch_backend('TkAgg')


if __name__ == "__main__":
main()
