import random
from replit import clear
from art import logo


def deal_card():
  """Returns a random card from the deck"""
  cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
  card = random.choice(cards)
  return card

# Hint : 3 create a function called calculate_score() that takes a List of cards as input and returns the score.

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if sum(cards) == 21 and len(cards) == 2:
    return 0   # Black jack
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  return sum(cards)

def compare(user_score, computer_score):
  if user_score == computer_score:
    return "Draw"
  elif computer_score == 0:
    return "Lose, opponent has Blackjack!"
  elif user_score == 0:
    return "Win with a Blackjack!"
  elif user_score > 21:
    return "You went over. You lose!"
  elif computer_score > 21:
    return "Opponent went over. You win!"
  elif user_score > computer_score:
    return "You win!"
  else:
    return "You lose!"

# Hint 2: Deal the user and computer 2 cards each using deal_card() and append().

# user_cards = []
# computer_cards = []


# for _ in range(2):
#   user_cards.append(deal_card())
#   computer_cards.append(deal_card())


# Hint 4 :  call calculate_score(). If the computer or the user has a black jack (0) or if the user's score is over 21, then the game ends
def game_initialize():
  print(logo)
  user_cards = []
  computer_cards = []


  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())

  is_game_over = False
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
    
    # Hint 5:  if the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Type 'hit' to get another card, type 'hold' to pass: ")
      if user_should_deal == "hit":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(f" Your final hand: {user_cards}, final score: {user_score}")
  print(f" Computer's final hand: {computer_cards}, final score: {computer_score}")
  print(compare(user_score, computer_score))
  
while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    game_initialize()