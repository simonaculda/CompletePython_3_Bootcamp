import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True


class Card:

    def __init__(self, suit, ranks):
        self.suit = suit
        self.ranks = ranks
        # self.values = values

    def __str__(self):
        return self.ranks + ' of ' + self.suit


class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ''
        for cart in self.deck:
            deck_comp += '\n' + cart.__str__()  # str(cart)
        return deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        single_card = self.deck.pop()
        return single_card


class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.ranks]
        # track aces
        if card.ranks == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:  # self.aces >0
            self.value -= 10
            self.aces -= 1


class Chips:

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("How many chips would you like to bet?  "))
        except:
            print("Sorry please provide am integer")
        else:
            if chips.bet > chips.total:
                print("Sorry, you haven't enough chips! You have: {}".format(chips.total))
                # continue
            else:
                break


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Hit or Stand? Enter h or s")
        if x[0].lower() == 'h':
            hit(deck, hand)
        elif x[0].lower() == 's':
            print("Player Stands \nDealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that!\n Please enter h or s only ")
            continue
        break


def player_bust(player, dealer, chips):
    print('BUST PLAYER')
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("PLAYER WINS")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("BUST DEALER \n PLAYER WINS")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("DEALER WINS")
    chips.lose_bet()


def push(player, dealer):
    print('Dealer and player tie! PUSH')


def show_some(player, dealer):
    print("DEALER'S HAND")
    print("ONE CARD HIDDEN!")
    print(dealer.cards[1])
    print("\n")
    print("PLAYER HAND")
    for card in player.cards:
        print(card)


def show_all(player, dealer):
    print("Player hand:")
    for card in player.cards:
        print(card)
    print("\n")
    print("Dealer hand:")
    for card in dealer.cards:
        print(card)


while True:
    # Print an opening statement
    print("WELCOME TO TE BLACKjACK GAME")
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    player_hand = Hand()
    dealer_hand = Hand()
    for i in range(0, 2):
        player_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())
    # Set up the Player's chips
    player_chips = Chips()
    # Prompt the Player for their bet
    take_bet(player_chips)
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand, dealer_hand)
    while playing:  # recall this variable from our hit_or_stand function
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck, player_hand)
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_bust(player_hand, dealer_hand,player_chips)
            break
    if player_hand.value <= 21:
        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
        while dealer_hand.value < 17:
            hit(deck, dealer_hand)

        # Show all cards
        show_all(player_hand, dealer_hand)
        # Run different winning scenarios
        if player_hand.value > dealer_hand.value:
            player_wins(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > 21:
            dealer_busts(player_hand, dealer_hand, player_chips)
        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand, dealer_hand, player_chips)
        else:
            push(player_hand, dealer_hand)
        # Inform Player of their chips total
    print("Player total chips are at :{}".format(player_chips.total))
    # Ask to play again
    new_game = input("Would you like to play again? y/n")
    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank you for playing")
        break




# test_deck = Deck()
# test_deck.shuffle()
# print(test_deck)
# # Player
# test_player = Hand()
# test_player.add_card(test_deck.deal())
# print(test_player.value)
# # print(test_deck)
# print("The card we show is " + test_deck.deal().__str__())