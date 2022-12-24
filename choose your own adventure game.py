name = input('What is your name? ')
print(f'Welcome', name, 'to this adventure!')

answer = input('You are on a dirt road and it has come to an end. You can go left or right. Which way would you like to go? ').lower()

if answer == 'left':
    answer = input('You come to a river. You can either walk around it or swim across it. Type walk to walk around or swim to swim around. ').lower()
    if answer == 'swim':
        print('You swam across and were eaten by an alligator.')
    elif answer == 'walk':
        print('You walked for many miles and ran out of water. You lost the game.')
    else:
        print('Not a valid option. You lost.')
elif answer == 'right':
    answer = input('You come to a bridge. It looks very unstable. Do you want to cross it or go back? (cross/back): ').lower()
    if answer == 'cross':
        answer = input('You ran across the bridge as fast as you could. You made it across safely, but the bridge is now destroyed. A stranger approaches you. Do you talk to them? (yes/no) ').lower()
        if answer == 'yes':
            print('You talked to the stranger and they gave you some gold. You WON!')
        elif answer == 'no':
            print('You ignored the stranger and walked past them. You end up getting lost and regret not talking to the stranger. You LOSE.')
        else:
            print('Not a valid option. You lost.')

    if answer == 'back':
        print('You went back to the main road. You lose.')
    else:
        print('Not a valid option. You lost.')

else:
    print('Not a valid option. You lost.')

print(f'Thank you for playing', name)