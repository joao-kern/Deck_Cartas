from datetime import datetime

class Deck:
    def __init__(self):
        pass

    def run(self):
        while continue_program:
            variable = datetime.now()
            deck, deck_por_naipe = self.create_deck()
            deck_embaralhado = deck[:]
            deck_embaralhado = self.shuffle_deck(deck_embaralhado, variable)
            self.get_deck(deck_embaralhado)
            self.get_some_cards(deck_embaralhado)

    def operacoes(self, op):
        if op == 1:
            self.shuffle_deck()
        elif op == 2:
            self.get_deck()
        elif op == 3:
            self.continue_program()

    def create_deck(self):
        deck = []
        deck_por_naipe = []
        for naipe in ("♥", "♦", "♣", "♠"):
            cartas_naipe = []
            for value in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"):
                cartas_naipe.append(f"{naipe+value}")
                deck.append(f"{naipe+value}")
            deck_por_naipe.append(cartas_naipe)
        return deck, deck_por_naipe
    
    def get_deck(self, deck):
        print(deck)

    def shuffle_deck(self, deck_embaralhado, variable):
        for i in range((len(deck_embaralhado) - 1), -1, -1):
            new_place = variable.second % (i + 1)
            deck_embaralhado[i], deck_embaralhado[new_place] = deck_embaralhado[new_place], deck_embaralhado[i]
        return deck_embaralhado
    
    def get_some_cards(self, deck):
        num_cards = int(input('Digite quantas cartas desejas pegar: '))
        cards_chosen = ''
        for i in range(num_cards):
            cards_chosen += f"{deck[i] } "
        print(f'Cartas que foram pegas: {cards_chosen}')

    def continue_program(self):
        gonna_continue = input('Digite se quer continuar(S/N): ').upper().split()
        if gonna_continue == "N":
            return False
        return True