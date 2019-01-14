import logging
from time import asctime
from random import randint
from battle import Battle
from models.army import Army
from mylogger import mylogger


if __name__ == '__main__':

    session = ''.join(asctime().split()).replace(':', '_')
    log_info = mylogger(session, 'info')
    log_debug = mylogger(session, 'debug')
    log_error = mylogger(session, 'error')

    armies = []
    try:
        calc_army = input('Enter how many armies are playing (min = 2): \n')
        calc_army = int(calc_army)
        if calc_army < 2:
            log_error.error('Entered less then 2 armies')
            print('You entered less then 2 armies')
        else:
            mode = input('Do you want to create army by hand?(Y/N): \n')
            for i in range(calc_army):
                if mode.upper() == 'Y':
                    calc_squad = int(
                        input(
                            'Enter how many squads for Army_{0} (min = 2):\n'.format(i))
                    )
                else:
                    calc_squad = randint(2, 10)
                army = Army(calc_squad, i)
                log_info.info('{0}, Squads: {1}\n'.format(army, army.squads))
                army.create_army(log_info)
                army.damage_rank()
                armies.append(army)

            Game = Battle(armies)
            Game.battle_armies(log_debug)
            log_debug.debug('{}'.format(Game))
            print(Game)
    except ValueError:
        log_error.error('Wrong input format: {}'.format(calc_army))
        print('Wrong input, you must input only number')
