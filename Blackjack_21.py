#Created by Alliance82
#Created on 12/26/2023
#This program builds a 52 card, 4 suit deck with numeric and face card values

import random
import os
import numpy as np
import pprint

# Clear the terminal
def clear():
    os.system("clear")

print("Alliance82 Presents Twenty-One. The Game Starts Now!")

card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["clubs", "diamonds", "hearts", "spades"]
suits_value = {"spades":"\u2664", "hearts":"\u2661", "clubs": "\u2667", "diamonds": "\u2662"}
card_scores = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 11
}
player_hand=[]
player_hand_image=[]
total_score = 0
score = []
 
class Card:
    def __init__(self, value, suit, suits_value):
        self.value = value
        self.suit = suit
        self.suits_value = suits_value

def generate_cards():
    cards = []
    for value in card_values:
        for suit in suits:
            _card = Card(value, suit, suits_value[suit])
            cards.append(_card)
    return cards

cards = generate_cards()
#Shuffle the deck
random.shuffle(cards)

#Proof the full deck is constructed
#print("Here's all the cards in the deck:")
#for card in cards:
#    print(card.value, card.suit, card.suits_value)
#print("Here's how many cards are in the deck:")
#print(len(cards))

#Draw a Card 
def draw():
    selected_card = vars(cards[0])
    remove_card = cards[0]
    selected_card_suit_name=selected_card.get('suit')
    selected_card_value=selected_card.get('value')
    selected_card_suit=selected_card.get('suits_value')
    selected_card_image=("____________"
       +"\n|            |"
       +"\n| {}{}         |".format(selected_card_value,selected_card_suit)
       +"\n|            |"
       +"\n|            |"
       +"\n|         {}{} |".format(selected_card_value,selected_card_suit)
       +"\n|____________|")
    #print(selected_card_image)
    cards.remove(remove_card)

    player_hand.append(selected_card)
    player_hand_image.append(selected_card_image)
    
    #print("This is the player hand:")
    #Prints the Hand
    #for x in player_hand_image:
    #    print(x)
    
    #Prints the Score
    for x in player_hand:
        value = x['value']

    print(f"You drew:\n {selected_card_image}")
    score.append(card_scores[value])
    total_score = sum(score)
    return total_score


#Scoring and gameplay
while True:
    draw_again = input(f"Would you like to hit (Y/N):")
    if draw_again.upper() == 'Y':
       player_score = draw()
       print(f"The player score is {player_score}.")
       if player_score == 21:
          print("Winner Winner Chicken Dinner! Blackjack!!")
          break
       elif player_score > 21:
          print("You Lose")
          break
    elif draw_again.upper() == 'N':
        print(f"Your total score was {player_score}.")
        total_score = 0
        score = []
        player_hand = []
        player_hand_image = []
        dealer_score = draw()
        if player_score == 21:
            print("Winner Winner Chicken Dinner! Blackjack!!")
            break
        elif player_score > 21:
            print("You Lose")
            break
        else:
            dealer_score = draw()

            if dealer_score > 21:
                print("The dealer busted. You win!")
                break
            elif dealer_score == 21:
                print("The dealer won this round")
                break
            elif dealer_score > player_score:
                print(f"The dealer won this round. The dealer had {dealer_score} and you had {player_score}")
                break
            elif dealer_score < player_score:
                dealer_score = draw()
                print(f"Round Update. The dealer has {dealer_score} and you had {player_score}")
                break
            else:
                print(f"The dealer: {dealer_score}. Your score: {player_score}.")
                break                
        break
    else:
        print("Invalid choice. Please enter y or n.")