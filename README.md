# Stock-Trading-App
A command-line stock trading application that allows users to practice and simulate stock trading without risking real money. The app uses real-time market data to let users manage a virtual portfolio, execute trades, and analyze historical stock trends. All user data is persistently stored locally so that profit and loss can be tracked over time.

Features
View Portfolio: Check your current stock quantities, purchase dates, purchase prices, and net profit/loss.  

Buy Stocks: Purchase stocks using real-time data fetched via the yfinance library. The app prompts for the stock symbol and quantity, calculates the total cost, and requires user confirmation.  

Sell Stocks: Sell your shares at current market prices, complete with a confirmation prompt to finalize the transaction.  

Historical Data: View historical stock prices by entering a specific stock and a period of days. Users also have the option to plot this data visually.  

Data Persistence: Automatically stores and loads portfolio data using a portfolio.json file, ensuring no data is lost between sessions.  

Transaction Timestamps: Every transaction automatically notes the exact date and time it was executed.  

Prerequisites
To run this application, you will need to have the following Python libraries installed:
yfinance: For fetching real-time and historical market data.  

matplotlib: For rendering visual plots of historical stock data.  

How to Run
To start the application, navigate to the project directory in your command line and run the following command: Python3 main.py

Challenges and Future Work
Add more efficiency and consistency in data handling.  

Implement a proper database to store portfolio data, replacing the current hard-to-read JSON implementation.  

Enhance the command-line interface to make it faster and more user-friendly.  

Introduce advanced options such as side-by-side stock comparisons and future price predictions using trading algorithms and graph mathematics.  

Add a secure login page so multiple users can operate the app from a single device securely.  

Increase the overall security of the application
