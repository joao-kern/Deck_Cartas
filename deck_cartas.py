from datetime import datetime

class Deck:
    def __init__(self):
        self.continue_program = False
        self.deck = self.create_deck()
        self.deck_copy = self.deck[:]
        self.variable = datetime.now()
        self.quant_players = 0
        self.players_cards = []
        pass

    def run(self):
        self.continue_program = True
        while self.continue_program:
            print('Menu Operações')
            print('1 - Embaralhar cartas')
            print('2 - Ver o deck (Ignorando a distribuição para os jogadores)')
            print('3 - Ver o deck (levando em conta a distribuição para os jogadores)')
            print('4 - Distribuir para jogadores')
            print('5 - Ver as cartas dos jogadores')
            print('6 - Reiniciar decks')
            print('7 - Encerrar programa')
            verification = False
            while not verification:
                op = int(input('Digite a operação que deseja fazer: '))
                verification = self.verify_ops(op)
            self.operations(op)

    def operations(self, op):
        if op == 1:
            self.shuffle_deck()
        elif op == 2:
            self.get_deck_with_players_cards()
        elif op == 3:
            self.get_deck_without_players_cards()
        elif op == 4:
            self.distribute_cards()
        elif op == 5:
            self.get_players_decks()
        elif op == 6:
            self.restart_decks()
        elif op == 7:
            self.finish_program()

    def verify_ops(self, op):
        if 0 > op or op > 7:
            print('*Operação Impossível*')
            return False
        elif op == 4 and len(self.deck) != 52:
            print('*Deck precisa ser resetado para fazer essa operação novamente*')
            return False
        elif (op == 5 or op == 3) and self.quant_players == 0:
            print('*Cartas ainda não foram distribuídas para os jogadores*')
            return False
        return True

    def create_deck(self):
        deck = []
        for naipe in ("♥", "♦", "♣", "♠"):
            cartas_naipe = []
            for value in ("2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"):
                cartas_naipe.append(f"{naipe+value}")
                deck.append(f"{naipe+value}")
        return deck
    
    def get_deck_with_players_cards(self):
        print('')
        print('Deck: ')
        print('')
        print(self.deck_copy)
        print('')

    def get_deck_without_players_cards(self):
        print('')
        print('Deck: ')
        print('')
        if len(self.deck) ==  0:
            print('Não há mais cartas sobrando no deck')
        else:
            print(self.deck)
        print('')

    def shuffle_deck(self):
        if len(self.deck) == 0:
            print('')
            print('Não há como embaralhar o deck porque não tem mais cartas')
            print('')
        else:
            for i in range((len(self.deck) - 1), -1, -1):
                new_place = self.variable.microsecond % (i + 1)
                self.deck[i], self.deck[new_place] = self.deck[new_place], self.deck[i]
                self.deck_copy[i], self.deck_copy[new_place] = self.deck_copy[new_place], self.deck_copy[i]
            print('')
            print('Deck embaralhado com sucesso!')
            print('')
    
    def distribute_cards(self):
        self.quant_players = int(input('Digite a quantidade de jogadores: '))
        verification = False
        while not verification:
            num_cards = int(input('Digite quantas cartas desejas pegar: '))
            verification = self.verify_num_cards(num_cards)
        self.players_cards = []
        for i in range(self.quant_players):
            player_cards = []
            for j in range(num_cards):
                player_cards.append(self.deck[0])
                self.deck.remove(self.deck[0])
            self.players_cards.append(player_cards)
        print('Cartas distribuidas com sucesso!')
        print('')

    def verify_num_cards(self, num_cards):
        if num_cards * self.quant_players > 52:
            print('*Quantidade de cartas que seriam distribuidas ultrapassa as 52 cartas presentes no deck*')
            return False
        return True

    def get_players_decks(self):
        for i in range(self.quant_players):
            print('')
            print(f'Cartas Jogador {i+1}:')
            print('')
            print(self.players_cards[i])
        print('')

    def restart_decks(self):
        self.create_deck()
        self.quant_players = 0
        self.players_decks = []
        print('')
        print('Deck desembaralhado e cartas dos jogadores devolvidas ao deck')
        print('')

    def finish_program(self):
        self.continue_program = False