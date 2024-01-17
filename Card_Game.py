import random

# Global Variables
suits = ['DIAMONDS', 'CLUBS', 'HEARTS', 'SPADES']
values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K']

# Class called Deck
class Deck:
    # Default Constructor 
    def __init__(self):
        self.deckOfCards = [] #Empty deck of cards

    # Method to generate a 52 card deck
    def generate_deck(self):
        for suit in suits:
            for value in values:
                self.deckOfCards.append(Card(suit, value))
        
    # Method to draw one or more cards from the deck
    def draw_card(self):
        return self.deckOfCards.pop()

    # Method to Shuffle deck of cards
    def shuffle_deck(self):
        random.shuffle(self.deckOfCards)

    # Method to "reset" the deck back to the orginal 52 cards
    def reset(self):
        self.deckOfCards.clear()
        for suit in suits:
            for value in values:
                self.deckOfCards.append(Card(suit, value))

        self.shuffle_deck()

     # Implement the __len__ method for the Deck
    def __len__(self):
        return len(self.deckOfCards)


class Hand:
    # Default Constructor
    def __init__(self):
        self.user_hand =[] #Empty users hand

    # Method to draw 1 from deck of cards
    def draw(self, deck):
        for draw in range(1):
            self.user_hand.append(deck.draw_card())
    
    # Method to add total points together (user_hand)
    # Didn't want to do elif because I would have to do a else statement
    # Use the built-in sum()
    def add_hand(self):
        user_points = []
        score = 0
        for card in self.user_hand:
            if card.value == 'A':
                points = 1
            elif card.value in ['J', 'Q', 'K']:
               points = 10
            else:
                points = card.value

            user_points.append(points)
            
            score = sum(user_points)
        return score
    
    # Implement the __len__ method for the Hand
    def __len__(self):
        return len(self.user_hand)


class Card:
    # Default Constructor
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    # __add__ method to allow summing two card or one card and integer and an object
    """?????????????????????????????????????"""
    def __add__(self, other):
        if int(other) == Card:
            return int(self.value + other.value)
        elif int(other) == int:
            return int(self.value + other)
        else:
            return NotImplemented

    # __radd__ method (having both add and radd will allow sum() to used on an iterable of Cards)
    def __radd__(self, other):
        return self.__add__(other)


class Dealer:
    # Default Constructor
    def __init__(self):
        self.dealer_hand =[] #Empty users hand

    # Method to draw 1 from deck of cards
    def draw(self, deck):
        for draw in range(1):
            self.dealer_hand.append(deck.draw_card())

    # Method to add total points together (user_hand)
    # Didn't want to do elif because I would have to do a else statement
    # Use the built-in sum()
    def add_hand(self):
        dealer_points = []
        score = 0
        for card in self.dealer_hand:
            if card.value == 'A':
                points = 1
            elif card.value in ['J', 'Q', 'K']:
               points = 10
            else:
                points = card.value

            dealer_points.append(points)
            
            score = sum(dealer_points)
        return score
    
    # Method to discard a card from the hand
    def remove_card(self):
        return self.dealer_hand.pop()
    
    # Place card back
    def place_card_back(self, card):
        self.dealer_hand.append(card)
    

def dealer_logic():
    dl.place_card_back(removed)
    dealer_score = dl.add_hand()
    
    # While loop until dealer score is not greater than 17
    while dealer_score < 17:
        dl.draw(d)
        dealer_score = dl.add_hand()

        # If dealer hand is greater than 21
        if dealer_score > 21:
            print("\nDealer's Hand")
            for card in dl.dealer_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')
            
            print(f"\nTotal Dealer points: {dealer_score}")

            print("\nUser's hand")
            for card in h.user_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')

            print(f"\nTotal player's points: {player_score}")

            print("\nDealer BUSTED!!! PLAYER WINS!!!")

            break

        # If dealer hand is equal to 21
        if dealer_score == 21:
            print("\nDealer's Hand")
            for card in dl.dealer_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')
            
            print(f"\nTotal Dealer points: {dealer_score}")

            print("\nUser's hand")
            for card in h.user_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')

            print(f"\nTotal player's points: {player_score}")

            print("DEALER HAS A BLACKJACK!!! PLAYER LOSES")

            break

        # If dealer hand is equal to player score
        if dealer_score == player_score:
            print("\nDealer's Hand")
            for card in dl.dealer_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')
            
            print(f"\nTotal Dealer points: {dealer_score}")

            print("\nUser's hand")
            for card in h.user_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')

            print(f"\nTotal player's points: {player_score}")

            print("\nTIE GAME!!!")

            break

        # If player score is greater than dealer score player wins
        if player_score > dealer_score:
            print("\nDealer's Hand")
            for card in dl.dealer_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')
            
            print(f"\nTotal Dealer points: {dealer_score}")

            print("\nUser's hand")
            for card in h.user_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')

            print(f"\nTotal player's points: {player_score}")

            print("\nPLAYER SCORE HIGHER!!! YOU WIN!!!")

            break


if __name__ == "__main__":
    # Created instances (Like C++ with class obj)

    d = Deck()
    h = Hand()
    dl = Dealer()

    player_score = 0
    dealer_score = 0

    # Call Functions to generate cards, shuffle deck, and show deck
    d.generate_deck()
    d.shuffle_deck()

    # Deal two cards to player and dealer at the beginning of the game
    for i in range(2):
        h.draw(d)
        dl.draw(d)

    # Add hands up for player
    player_score = h.add_hand()

    removed = dl.remove_card()

    # Add hands up for dealer
    dealer_score = dl.add_hand()

    blackJack = True
    
    # Full game logic for player
    while blackJack:
        print("\nBlack Jack Game")
        print("--------------------")

        print("A equal to 1 point")
        print("J, Q, K equal to 10 points")

        print("\nDealer's Hand")
        for card in dl.dealer_hand:
            print(f'{card.suit.center(8)}   Value and Points: {card.value}')
        
        print(f"\nTotal Dealer points: {dealer_score}")
        
        print("\nUser's hand")
        for card in h.user_hand:
            print(f'{card.suit.center(8)}   Value and Points: {card.value}')

        print(f"\nTotal player's points: {player_score}")

        print("\nEnter in choice below:")
        choice = input("H for Hit or S for Stand: ")

        if choice.upper() == 'H':
            h.draw(d)
            player_score = h.add_hand()
            print("\nPlayer: Hit me")

        if choice.upper() == 'S':
            print("\nPlayer: I Stand")
            dealer_logic()
            break

        # If player score is equal to 21 they win the game
        if player_score == 21:
            dl.place_card_back(removed)
            dealer_score = dl.add_hand()
            print("Dealer's Hand")
            for card in dl.dealer_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')

            print(f"\nTotal Dealer points: {dealer_score}")

            print("\nUser's hand")
            for card in h.user_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')

            print(f"\nTotal player's points: {player_score}")

            print("\nYOU HAVE BLACKJACK!!! YOU WIN!!!")

            break

        # If the player score is greater than 21 they bust and lose the game
        if player_score > 21:
            dl.place_card_back(removed)
            dealer_score = dl.add_hand()
            print("Dealer's Hand")
            for card in dl.dealer_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')
            
            print(f"\nTotal Dealer points: {dealer_score}")

            print("\nUser's hand")
            for card in h.user_hand:
                print(f'{card.suit.center(8)}   Value and Points: {card.value}')

            print(f"\nTotal player's points: {player_score}")

            print("\nYOU BUSTED!!! GAME OVER!!!")

            break
