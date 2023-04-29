from turtle import begin_fill


print("Welcome To Secret Silent Auction Bidding!")

endTheAuction = False
players = {}

while endTheAuction is False:
    name = input("Enter The Name of the Player:  ")
    bid = int(input("Enter The Bid: $"))

    players[name] = bid

    decision = input("Are There Any Other Players (yes/no): ")
    if decision == "no":
        break

winner = max(players, key = players.get)

print(f"The Winner of The Auction is {winner} with a BID of ${players[winner]}")