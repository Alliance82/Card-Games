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

print("The program has started")

card_values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
suits = ["clubs", "diamonds", "hearts", "spades"]
suits_value = {"spades":"\u2664", "hearts":"\u2661", "clubs": "\u2667", "diamonds": "\u2662"}
 
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

print("Here's all the cards in the deck:")
for card in cards:
    print(card.value, card.suit, card.suits_value)

print("Here's how many cards are in the deck:")
print(len(cards))

#Draw a Card 
def draw():
    selected_card = vars(cards[0])
    remove_card = cards[0]
    selected_card_suit_name=selected_card.get('suit')
    selected_card_value=selected_card.get('value')
    selected_card_suit=selected_card.get('suits_value')
    selected_card_image=(" ____________"
       +"\n|            |"
       +"\n| {}{}         |".format(selected_card_value,selected_card_suit)
       +"\n|            |"
       +"\n|            |"
       +"\n|         {}{} |".format(selected_card_value,selected_card_suit)
       +"\n|____________|")
    print(selected_card_image)
    cards.remove(remove_card)
print("We are about to draw that card:")
draw()
print("Here's how many cards are left in the deck:")
print(len(cards))
draw_again = input("Would you like to draw another card (Y/N):")
#response=draw_again.upper()
while draw_again.upper() == 'Y':
    draw()
    draw_again = input("Would you like to draw another card (Y/N):")
    print("Here's how many cards are left in the deck:")
    print(len(cards))
else:
    print("Buonanotte")