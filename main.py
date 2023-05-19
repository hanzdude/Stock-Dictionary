def intro():
  
  print ("Welcome to Stock Checker. \nThis checks the current stock price of the top 20 stocks in the S&P 500.")

stocks_dict = {
  'AAPL': '165.17',
  'MSFT': '281.16',
  'AMZN': '106.34',
  'NVDA': '269.93',
  'GOOGL': '106.26',
  'BRK.B': '325.36',
  'GOOG': '106.98',
  'TSLA': '161.19',
  'META': '212.74',
  'XOM': '118.32',
  'UNH': '487.93',
  'JNJ': '163.35',
  'JPM': '140.43',
  'V': '232.57',
  'PG': '156.17',
  'MA': '374.69',
  'CVX': '171.61',
  'HD': '300.43',
  'ABBV': '164.12',
  'LLY': '382.56'
}
# top 20 S&P 500 stocks with their prices as of 04/24/23
intro()

def main():

  stock = input("Please enter the ticker symbol of the stock you'd like to check:").upper()

#I found this stack overflow page for converting user inputs to capitalization to clean up the code and also make it less likely the user encounters an error. https://stackoverflow.com/questions/8772142/converting-to-upper-case-which-way-is-more-pythonic

  try:

    price = stocks_dict[stock]
    print (f"The current price for {stock} is ${price}.")

  except:
    print ("Sorry, we couldn't find that stock price. Please check your spelling and try again.")
    main()

  outro()

negative = ["no", "nope", "naw", "nah", "negative"]

positive = ["yes", "yeah", "yup", "sure"]

#possible responses for the outro

def outro():
    compute_again = (input("Would you like to check another stock price? ")).lower()
  
    if compute_again in negative:
      print ("Thanks for using Stock Checker!")
      exit()

    elif compute_again in positive:
      print()
      main()

    else:
      print()
      print ("Sorry, that isn't a recognized input")
      print()
      outro()

main()

#this code was re-used from the homework video and the outro() function was reused from my submission last week. I cleaned up the "affirmative" and "negative" lists by adding the .lower() to the end of my outro user input.