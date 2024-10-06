from datetime import datetime

class Deck:
    def __init__(self):
        self.deck = self.create_deck()
        self.deck_copy = self.deck[:]
        self.variable = datetime.now()
        self.quant_players = 0
        self.players_cards = []

    def create_deck(self):
        deck = []
        for naipe in ("♥", "♦", "♣", "♠"):
            for value in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"):
                deck.append(f"{naipe+value}")
                
        return deck

    def get_deck(self):
        return self.deck
    
    def get_deck_copy(self):
        return self.deck_copy

    def get_len_deck(self):
        return len(self.deck)

    def get_quant_players(self):
        return self.quant_players
    
    def get_player_cards(self):
        return self.players_cards

    def shuffle_deck(self):
        if len(self.deck) == 0:
            return False
        else:
            for i in range((len(self.deck) - 1), -1, -1):
                new_place = self.variable.microsecond % (i + 1)
                self.deck[i], self.deck[new_place] = self.deck[new_place], self.deck[i]
            self.deck_copy = self.deck[:]

            return True
    
    def distribute_cards(self, quant_players, num_cards):
        self.quant_players = quant_players
        self.players_cards = []
        for i in range(quant_players):
            player_cards = []
            for j in range(num_cards):
                player_cards.append(self.deck[0])
                self.deck.remove(self.deck[0])
            self.players_cards.append(player_cards)

    def restart_decks(self):
        self.deck = self.create_deck()
        self.deck_copy = self.deck[:]
        self.quant_players = 0
        self.players_decks = []
