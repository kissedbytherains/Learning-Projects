def hidden_auction():
  auction = True
  auction_dict = {}
  auc_list = []
  while auction:
    Bidder = input(f"What is your name?: ")
    Bid = int(input(f"What is your bid?: "))
    auc_list.append(Bid)
    auction_dict[Bidder] = Bid
    cont = input(f"Are there any other bidders? Type 'yes' or 'no' ").lower()
    if cont == "yes":
      #clear()
      continue
    else:
      auction = False
      #clear()
  big_bid = 0
  for i in auc_list:
    if i > big_bid:
      big_bid = i
  big_bidder = list(auction_dict.keys())[list(auction_dict.values()).index(big_bid)]
  return(f"The highest bidder is {str(big_bidder)}, with a bid of {big_bid}")
print(hidden_auction())
