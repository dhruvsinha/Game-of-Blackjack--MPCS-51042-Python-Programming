"""
I would like to give credit to several people who have assisted me in this project.
David Hackett was kind enough to take out time and help me out with some very
minute details. I also want to thank Professor Rahman for conducting office hours
and classes on this topic. The discussion on ED also helped with several small
clarifications so I would like to thank everyone for their questions.

I am also very grateful to several instructors on YouTube who helped me conceptually
as well as contexually. Here are the links of a few videos and and their github profile.

https://github.com/sush3011/Python-Practice/blob/master/blackjack.py
https://www.youtube.com/watch?v=C82s5WufNUA&t=95s
https://www.youtube.com/watch?v=yJz2at4Hco4
https://i.ytimg.com/an_webp/8QTsK1aVMI0/mqdefault_6s.webp?du=3000&sqp=CPmbjYwG&rs=AOn4CLC5b_LPKCvUdgBnFDEHpLDYY5DYbg

"""
from random import shuffle
from abc import ABC, abstractmethod

suits = ('\u2665', '\u2666', '\u2660', '\u2663')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:  # Creates all the cards
    
    """This class creates an istance of a card
    
    In this class, we create an instance of each card. The attribute of each card
    is taken from the suits and ranks that we have defined in suits and ranks 
    glabal variables

    
    Attributes
    --------------
    suit: a unicode character
          This is one of the characters for clubs, diamonds, spades, or hearts
    rank: str
          rank consists of rank of the card in string
    """
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank


    def __str__(self):
        
        """This method returns the card instance
        
        Using this method, we return the instance of the card we created in the
        constructor in the form of a string. 
        
        Returns
        -------
        str
            This function returns a string that captures the rank and suit of 
            the card. So the string is of the format: "[rank] of [suit]"

        """
        return self.rank + ' of ' + self.suit
    

class Deck:  # creates a deck of cards
    """In this class, we create the complete Deck of all the cards. 
    
    While creating a deck instance, we call upon the Card Class multiple times
    and store each card instance in the Deck Instance list. This Class also has 
    methods that will allow us to suffle the deck, get a card from the deck, and 
    also deal from the top of the deck.
    
    Attributes
    ------------
    deck:LIST
        We will store all the cards in the deck and use this deck to deal and 
        play blackjack
    """
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __getitem__(self, position):
        """
        This method returns the card available in the deck at the specified
        position
        
        Parameters
        ------------
        position: int
                  the 'card number' in the deck that we wish to get
        
        Returns
        -----------
        Str- 
            This method will return the card available at the 'position' index
            in the deck
        """
        return self.deck[position]

    def shuffle(self):  # shuffle all the cards in the deck
        """
        This method shuffles the deck by invoking shuffle from random
        """
        shuffle(self.deck)


    def deal(self):  # pick out a card from the deck
        """Deal a card
        
        In this method, we deal a card by selecting the top most card in the deck
        
        Returns
        ----------
        single_card: str
        This is the top card in the deck that will be added to Computer's, Human's
        or Dealer's hand
        """
        single_card = self.deck.pop(0)
        return single_card
#%%
class Game:
    """Initilize players and PLAY!!!
    
    In this class we will initialize human and computer players and also play
    the game of blackjack. The play() method will allow us to initiate a game
    between the dealer, human players and ciomputer player
    
    Attributes
    ------------
    n_human: int
            number of human players
    n_computer:int
               number of computer players
    """
    def __init__(self, n_human=2, n_computer=1):
        self.n_human=n_human
        self.n_computer=n_computer
        
        
    def play(self):
        """Play the game of blackjack!!
        
        In this method, we play the game of blackjack between the dealer,
        human players, and computer player. Here are the steps that we follow
        in the game- 
        
        a) create a list of human and computer players
        b) create a deck 
        c) give two cards to player and two cards to rach player one by one.
           Only the frst card of the dealer is visible to every player but 
           every player can see both the cards of every other player
        d) for each player, deal the cards until they stand or bust and print the hand
        e) store the score for each player
        f) After every player has finished playing, dealer plays the game by dealing
            cards for itself. They also deal until they bust or stand (they stand 
            when the score is between 17 and 21) 
        g) we store the score of dealer in the same dictionary as the scores of 
            other players
        h) we print the score for each player and also declare the winner. The 
            winner is the player/players who have the highest score and haven't 
            busted
        i) after we declare the winner, we ask the human players if they want to 
          play the game again or not. We will restart the game if atleast 50%
          human players want to restart the game.
        """
        
        PLAYER_LIST=dict()# we will store the player name and player instance in this dictionary
        
        #in this for loop, I am creating name and instance for each human player \n
        #and storing it in the player list
        for human in range (self.n_human):
            name="Human Player "+str(human+1)
            instance_human_player=HumanPlayer()
            PLAYER_LIST[name]=instance_human_player
            
        #in this for loop, I am creating name and instance for each computer player \n
        #and storing it in the player list dictionary  
        for computer in range (self.n_computer):
            name="Computer Player "+str(computer+1)
            instance_computer_player=ComputerPlayer()
            PLAYER_LIST[name]=instance_computer_player
        
        # create and shuffle deck
        deck = Deck()
        deck.shuffle()
        
        PLAYER_CONTINUE_GAME_LIST=[]#in this list, we will store response of human players if they wish to continue playing another game of blackjack
        dict_score=dict()#this dictionary will be used to store the score of each player- 'player name': score
        print("Welcome to BlackJack!")
        dealer_hand= Dealer()#creating an instance of the dealer 
        dealer_hand.hit(deck)#deal a card for the dealer
        dealer_hand.hit(deck)#deal another card for the dealer
        
        #in this for loop, we want to give 2 cards to every player one by one
        for card in range(1,3):
            for player_name,player_hand in PLAYER_LIST.items():
                player_hand.hit(deck)#deal one card
                print("\n{} cards of {}".format(card,player_name))
                player_hand.show_all()#show the current hand of the player
                PLAYER_LIST[player_name]=player_hand#update the main list of players with their respective 'current' hands
        
        #in the next line, we print half hand of the dealer. 
        print("\nDealers Half Hand:\n{}\nSecond card hidden".format(dealer_hand.cards[0]))
        
        #now every player has seen '2 cards hand' of all the other players and '1 card hand' of the dealer
        #now, the players will play
        
        for player_name in PLAYER_LIST:
            player_hand=PLAYER_LIST[player_name]
            print("\n{} is playing".format(player_name))
            playing=True
            print("\nI would like to remind you of your hand")
            player_hand.show_all()# we will print the current hand the player
            
            #The while loop does the following- 
            #Human players will play till they stand or bust
            #Computer players play till they reach the score of 17 or bust
            while playing:
                playing=player_hand.hit_or_stand(deck)
                print("\nHand of {}".format(player_name))
                player_hand.show_all()
                if player_hand.value > 21:
                    print("{} BUSTS!!".format(player_name))
                    break
            
            print("{} has finished playing".format(player_name))
            dict_score[player_name]= player_hand.value#store the score of the player
        
            
        #once the players have finished playing, its dealer's turn
        print("\nDealer is playing now")
        if dealer_hand.value <= 21:
            dealer_hand.hit_or_stand(deck)
        print("\ndealer has finished playing") 
        if dealer_hand.value>21:
                print("Dealer BUSTS!!")
        
        
        dict_score['Dealer']= dealer_hand.value
        print("\nWe have already seen the full hand of every player. Dealer's final full hand is:")
        dealer_hand.show_all()
        print ("\nDealer's score is ", dealer_hand.value)
        
        print ("\nAll the players and the dealer have finished playing. The most awaited results are.....")
        
        print("\nhere is the score of each player")
        print(dict_score)
        
        
        #in the following section, we declare the winners of this round. \n
        #The logic is the following- compare the score of each player with  \n
        #maximum score yet encountered (winner_score). If that score is more \n
        #than the max score, then store the player name and max score. It also \n
        #deals with cases where there are two winners; 
        
        WINNER_LIST=[]
        winner_score=0
        for key in dict_score:
            score=dict_score[key]
            if score>winner_score and score <= 21:
                winner_score=score
                WINNER_LIST.clear()
                WINNER_LIST.append(key)
            elif score==winner_score and score <=21:
                winner_score=score
                WINNER_LIST.append(key)
        
        #show the name of the winners if there are any
        if (len(WINNER_LIST)>0):
            print("Here are the winners:")
            for winner in WINNER_LIST:
                print(winner)
        else:
            print("No player won, everyone busted")
        
        #in the following section, we ask each human player if they wish to play the game again
        for key,value in PLAYER_LIST.items():
            is_human=isinstance(value, HumanPlayer)
            if is_human==True:    
                new_game = input("Hey {} Would you like to play again? Enter 'y' or 'n': ".format(key))
                if new_game[0].lower() == 'y':
                    PLAYER_CONTINUE_GAME_LIST.append(1)
                else:
                    PLAYER_CONTINUE_GAME_LIST.append(0)
        
        #if 50% or more human players wish to resume the game, then we resume the game
        if (len(PLAYER_CONTINUE_GAME_LIST)>0):
            if (sum(PLAYER_CONTINUE_GAME_LIST)/len(PLAYER_CONTINUE_GAME_LIST)>=0.50):#if 50% players agree to play
                print("Democracy says that we resume the game!")
                g=Game()
                g.play()
            else:
                print("Goodbye, game ends here!!")
#%%

class Player(ABC):
    """This abstract class acts as a base class to HumanPlayer, ComputerPlayer and Dealer
    classes
    
    In this class, we have methods that allow us to perform actions like hitting the deck,
    adding the card to hand, adjusting for ace, and also an abstract method which is 
    works differently for human player, computer player, and dealer.
    
    Attributes
    -----------
    cards: LIST
            List of all the cards that are present in the hand of the player
    value: integer
            Score of the hand of each player. This is calculated by adding the value
            of each rank
    aces: integer
            Number of aces present in the hand of the player or the dealer.  
    """
    def __init__(self):
        self.cards=[]
        self.value=0
        self.aces=0
    
    
    def add_card(self,card):# add a card to players or dealers hand
        """Add a card to the list of cards
        
        This method allows us the add a card that we want to add to the player's hand (cards)
        
        Parameters
        -----------
        card: str
              this card is added to the player's hand
        """
        self.cards.append(card)
        self.value += values[card.rank]
        
        if card.rank == 'Ace':
            self.aces+=1
    
    def adjust_for_ace(self):
        """Adjust the value of ace
        
        This method adjusts the value of ace: the value of ace can be 1 or 11
        If the total score by taking ace=11 is exceding 21 then we consider
        ace the value of ace to be 1 and recalculate the score of the hand
        """
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1
    
    def hit(self,deck):
        """Hit the deck and deal a card
        
        This method calls upon add_card and passes along a card in that call. 
        The purpose of this method is to deal a card from the deck and then add to 
        the hand of the player
        
        Parameters
        -----------
        deck: instance of deck class
                we will deal a card from this deck
        """
        self.add_card(deck.deal())
        self.adjust_for_ace()
        
    def show_all(self):
        """Show all the cards
        
        Show all the cards that are present in the players/dealers hand
        """
        print(*self.cards, sep='\n')
        
    @abstractmethod
    def hit_or_stand(self, deck):
        """
        This abstract method, which is defined separately for the dealer, human player,
        and computer player, allows players to hit or stand based on their idea
        of the game. 
        
        Parameters
        -----------
        deck: instance of deck class
                the current deck that is in play so that users can deal from
                this deck
                
        Returns
        ---------
        playing: bool
                This will indicate when the while loop in the play method should
                come to a halt. We don't return anything when dealer is playing
        
        """
        pass
#%%
class HumanPlayer(Player):
        
    """Create an instance of the human player
    
    This class creates an instance of the human player. This class inherits all
    the methods defined in the Player Class. It also inherits an abstract method 
    hit_or_stand which is defined further in this class. This class allows the 
    human player to make a decision to whether hit or stand based on their 
    understanding of the game
    
    Attributes
    -----------
    Attributes for this class is same as that defined in the Player Class
    cards: LIST
            List of all the cards that are present in the hand of the player
    value: integer
            Score of the hand of the player. This is calculated by adding the value
            of each rank
    aces: integer
            Number of aces present in the hand of the player.  
    """
    
    def hit_or_stand(self,deck):
        """ Allows users to make decision to hit or stand
        
        This method allows the human player to make decision whether they want to hit
        or stand. If they hit, then we can add another card to their hand.
        
        Parameters
        ------------
        deck: instance of the deck method
              passes the current version of the deck as a parameter. The Human Player
              will be given cards from this deck.
        
        Returns
        ----------
        playing: boolean
                whenever player hits stand, boolean is False and the while loop
                in the play method of the Game method stops. If the player never
                stands, the playing variable is True and the while loop only stops
                when the player busts.
        """
        playing=True
        ask = input("\nWould you like to hit or stand? Please enter 'h' or 's': ")
            
        if ask[0].lower() == 'h':
            self.hit(deck)
            
        elif ask[0].lower() == 's':
            print("Player stands")
            playing = False
        else:
            print("Sorry! that response is not compatible. please input h or s")
        return playing    
#%%
class Dealer(Player):
    """Create an instance of the Dealer
    
    This class creates an instance of the Dealer. This class inherits all
    the methods defined in the Player Class. It also inherits an abstract method 
    hit_or_stand which is defined further in this class. This class allows the 
    dealer to deal cards for itself based on a few simple rules.
    
    Attributes
    -----------
    Attributes for this class is same as that defined in the Player Class
    cards: LIST
            List of all the cards that are present in the hand of the dealer
    value: integer
            Score of the hand of the dealer. This is calculated by adding the value
            of each rank
    aces: integer
            Number of aces present in the hand of the dealer.  
    """
    def hit_or_stand(self, deck):
        """Allows the dealer to deal based on some rules
        
        This method allows the dealer to make a hit decision. The dealer is dealt
        a card if their score is less than 17 and the dealing stops as soon as 
        the score crosses 17. Though this is very similar to the way Computer Player
        is playing in this case, a separate class makes sense because we can change
        the way computer player plays if we wish to.
        
        Parameters
        ------------
        deck: instance of the deck method
              passes the current version of the deck as a parameter. The Dealer
              will be given cards from this deck.
        """
        while (self.value<17):
            self.hit(deck)
#%%
class ComputerPlayer(Player):
    """Create an instance of the computer player
    
    This class creates an instance of the computer player. This class inherits all
    the methods defined in the Player Class. It also inherits an abstract method 
    hit_or_stand which is defined further in this class. This class deals card to
    the computer player based on a few simple rules.
    
    Attributes
    -----------
    Attributes for this class is same as that defined in the Player Class
    cards: LIST
            List of all the cards that are present in the hand of the player
    value: integer
            Score of the hand of the player. This is calculated by adding the value
            of each rank
    aces: integer
            Number of aces present in the hand of the player.  
    """    
    def hit_or_stand(self,deck):
        """Allows the Computer Player to deal based on some rules
        
        This method allows the Computer Player to make a hit decision. The Computer Player is dealt
        a card if their score is less than 17 and the dealing stops as soon as 
        the score crosses 17.
        
        Parameters
        ------------
        deck: instance of the deck method
              passes the current version of the deck as a parameter. The Computer Player
              will be given cards from this deck.
              
        Returns
        -----------
        playing: bool
                returns the boolean that determines when the player is going to
                stop playing
        """
        while (self.value<17):
            self.hit(deck)
        playing=False
        return playing
            
#%%
if __name__ == "__main__":
    g = Game()
    g.play()
#%%