# Object Oriented Programming- Game of Blackjack

## Project Abstract
In this project, I leverage Object Oriented Programming in Python to create a game of blackjack between human players, naive computer players, and a computer dealer. 

## Rules of the Game
For each round:
1. The dealer shuffles the deck.
2. The dealer gives 1 card face-up to all players; and 1 card face-up to themself.
3. The dealer gives 1 card face-up to all players; and 1 card face-down to themself.
4. For each player’s turn:
  - The player decides to “hit” (receive one more card from dealer) or “stand” (receive
  no more cards and immediately end their turn). If the player hits and their new
  score is > 21, then they “bust”, meaning that their turn immediately ends and they
  immediately lose.
  - Repeat until the player’s turn ends, either because they stand or bust.
5. For the dealer’s turn:
  - The dealer reveals their face-down card.
  - If the dealer’s score is ≥ 17, they must stand.
  - If the dealer’s score is < 17, they must continue to deal cards to themself until their
        score is ≥ 17. If their score ever becomes > 21, they bust and immediately lose.
5. Declare the winner of this round. The winner is the player or dealer with the highest
score.
6. Prompt the human players if they want another round.

## How to run

Download and run *python3 dhruv_blackj_FINAL.py*. You will see the instructions to play the game on the terminal. Enjoy!
