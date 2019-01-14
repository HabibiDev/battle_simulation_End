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
    armies = []
    try:
        calc_army = int(
            input('Enter how many armies are playing (min = 2): \n')
        )

        if calc_army < 2:
            print('You entered less then 2 armies')
        else:
            for i in range(calc_army):
                calc_squad = int(
                    input(
                        'Enter how many squads for Army_{0} (min = 2):\n'.format(i))
                )
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
        print('Wrong input, you must input only number')
