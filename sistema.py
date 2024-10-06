from deck_cartas import Deck

class Sistema:
    def __init__(self):
        self.continue_program = False
        self.deck = Deck()

    def run(self):
        self.continue_program = True
        self.operations = [
            self.shuffle,
            self.get_deck_with_players_cards,
            self.get_deck_without_players_cards,
            self.distribute_cards,
            self.get_players_cards,
            self.restart_decks,
            self.finish_program
        ]
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
                op = self.input_int('Digite a operação que deseja fazer: ')
                verification = self.verify_ops(op)
            
            self.operations[op-1]()

    def verify_ops(self, op):
        if 1 > op or op > 7:
            print('*Operação Impossível*')
            return False
        elif op == 4 and self.deck.get_len_deck() != 52:
            print('*Deck precisa ser resetado para fazer essa operação novamente*')
            return False
        elif (op == 5 or op == 3) and self.deck.get_quant_players() == 0:
            print('*Cartas ainda não foram distribuídas para os jogadores*')
            return False
        
        return True

    def shuffle(self):
        shuffled = self.deck.shuffle_deck()
        if shuffled:
            print('')
            print('Deck embaralhado com sucesso!')
            print('')
        else:
            print('')
            print('Não tem cartas no deck para embaralhar')
            print('')

    def distribute_cards(self):
        quant_players, num_cards = self.get_players_and_cards()
        self.deck.distribute_cards(quant_players, num_cards)
        print('')
        print('Cartas distribuidas com sucesso!')
        print('')

    def get_deck_with_players_cards(self):
        print('')
        print('Deck: ')
        print('')
        print(self.deck.get_deck_copy())
        print('')

    def get_deck_without_players_cards(self):
        print('')
        print('Deck: ')
        print('')
        if len(self.deck.get_deck()) ==  0:
            print('Não há mais cartas sobrando no deck')
        else:
            print(self.deck.get_deck())
        print('')
    
    def get_players_cards(self):
        players_cards = self.deck.get_player_cards()
        for i, player in enumerate(players_cards):
            print('')
            print(f'Cartas Jogador {i+1}:')
            print('')
            print(player)
        print('')
    
    def restart_decks(self):
        self.deck.restart_decks()
        print('')
        print('Deck desembaralhado e cartas dos jogadores devolvidas ao deck')
        print('')

    def finish_program(self):
        self.continue_program = False
        print('Programa finalizado.')

    def get_players_and_cards(self):
        verification = False
        while not verification:
            quant_players = self.input_int('Digite a quantidade de jogadores: ')
            num_cards = self.input_int('Digite quantas cartas desejas pegar: ')
            if num_cards * quant_players > 52:
                print('*Quantidade de cartas que seriam distribuidas ultrapassa as 52 cartas presentes no deck*')
            else:
                verification = True

        return quant_players, num_cards

    def input_int(self, question):
        while True:
            try:
                return int(input(question))
            except:
                print('*Valor digitado não válido*')
    