import random
from src.models.board import Board
from src.models.player import Player
from src.models.challenges import challenges
from src.services import utilities

game = Board()
turn_count = 1
P1 = Player()
P2 = Player()
P1.name = input('What is Player 1\'s name? ')
P2.name = input('What is Player 2\'s name? ')
players = [P1, P2]
starting_player = random.choice(players)


while turn_count < 10:
    print(f'The current turn is {turn_count}')
    current_player = utilities.determine_player(turn_count, starting_player, players)
    print(f'The current player is {current_player.name}.')

    print(f'{P1.name} has {P1.cards}')
    print(f'{P2.name} has {P2.cards}')

    selected_card = input('Choose a card from your hand ... ')
    while not utilities.has_card_in_hand(current_player, selected_card):
        selected_card = input('That card is not in your hand. Try again ... ')

    played_card = [item for item in current_player.hand if item['name'] == selected_card][0]
    print(f"{current_player.name} - {played_card['name']} ({played_card['id']})")

    selected_position = input('Choose a location ... ')
    while not utilities.position_is_available(game, selected_position):
        selected_position = input('There is already a card there. Try again ... ')

    utilities.place_card(game, current_player, played_card, selected_position)

    challenges(game, played_card, selected_position, P1, P2)

    print(game)

    turn_count += 1

print(utilities.determine_winner(game, P1, P2))