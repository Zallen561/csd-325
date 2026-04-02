"""Cho-Han, modified by Zach Allen
Original by Al Sweigart
"""

import random, sys

JAPANESE_NUMBERS = {1: 'ICHI', 2: 'NI', 3: 'SAN',
                    4: 'SHI', 5: 'GO', 6: 'ROKU'}

print('''Cho-Han, modified by Zach Allen

In this traditional Japanese dice game, two dice are rolled in a bamboo
cup by the dealer sitting on the floor. The player must guess if the
dice total to an even (cho) or odd (han) number.

*** NEW RULE: If you roll a 2 or 7, you get a 10 mon bonus! ***
''')  # Added bonus notice

purse = 5000
while True:  # Main game loop.
    print('You have', purse, 'mon. How much do you bet? (or QUIT)')
    while True:
        pot = input('za: ')  # Changed input prompt to initials
        if pot.upper() == 'QUIT':
            print('Thanks for playing!')
            sys.exit()
        elif not pot.isdecimal():
            print('Please enter a number.')
        elif int(pot) > purse:
            print('You do not have enough to make that bet.')
        else:
            pot = int(pot)
            break

    # Roll the dice.
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    print('The dealer swirls the cup and you hear the rattle of dice.')
    print('The dealer slams the cup on the floor.')
    print()
    print('    CHO (even) or HAN (odd)?')

    while True:
        bet = input('> ').upper()
        if bet not in ('CHO', 'HAN'):
            print('Please enter either "CHO" or "HAN".')
        else:
            break

    print('The dealer lifts the cup to reveal:')
    print('  ', JAPANESE_NUMBERS[dice1], '-', JAPANESE_NUMBERS[dice2])
    print('    ', dice1, '-', dice2)

    rollIsEven = (total % 2 == 0)
    correctBet = 'CHO' if rollIsEven else 'HAN'
    playerWon = bet == correctBet

    # BONUS RULE: If total is 2 or 7, add 10 mon
    if total == 2 or total == 7:
        print(f'BONUS! You rolled {total} and earned +10 mon!')
        purse += 10  # Add bonus to purse

    if playerWon:
        print('You won! You take', pot, 'mon.')
        purse += pot
        house_fee = pot * 12 // 100  # Changed house fee to 12%
        print('The house collects a', house_fee, 'mon fee.')
        purse -= house_fee
    else:
        purse -= pot
        print('You lost!')

    if purse == 0:
        print('You have run out of money!')
        print('Thanks for playing!')
        sys.exit()
