def main():
    Difficulty =  input("Difficult or Casual? ")
    if not (Difficulty == "Difficult" or Difficulty == "Casual"):
        print("Eneter a valid difficulty")
        return 
    
    Players = input("Multiplayer or Single-player? ")
    if not (Players == "Multiplayer" or Players == "Single-player"):
        print("Eneter a valid number of players")
        return 
    
    if Difficulty == "Difficult" and Players == "Multiplayer":
        recommend("Poker")
    elif Difficulty == "Difficult" and Players == "Single-player":
        recommend("Klondike")
    elif Difficulty == "Casual" and Players == "Multiplayer":
        recommend("Hearts")
    else:
        recommend("Clock")
      
      
def recommend(game):
    print("You might like", game)


main()

