def hidden_auction():
  auction = True
  auction_dict = {}
  while auction:
    Bidder = input(f"What is your name?: ")
    Bid = int(input(f"What is your bid?: "))
    auction_dict[Bidder] = Bid
    cont = input(f"Are there any other bidders? Type 'yes' or 'no' ").lower()
    if cont == "yes":
    #clear
      continue
    else:
      auction = False
      #clear
  big_bid = 0
  winner = ""
  for i in auction_dict:
    if auction_dict[i] > big_bid:
      big_bid = auction_dict[i]
      winner = i
  return(f"The highest bidder is {winner}, with a bid of {big_bid}")
print(hidden_auction())
