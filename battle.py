import logging


class Battle:

    def __init__(self, armies):
        self.armies = armies
        self.armies_game_over = []

    def battle_armies(self, log_debug):
        while len(list(set(self.armies) - set(self.armies_game_over))) > 1:
            for army in list(set(self.armies) - set(self.armies_game_over)):
                army.armies = list(
                    filter(
                        lambda x: x != army, (
                            set(self.armies) - set(self.armies_game_over)
                        )
                    )
                )
                target_army = army.choose_strategy()
                if target_army.is_active() != False:
                    target_army.attack_success(army, army.damage())
                else:
                    log_debug.debug('{0} out of game\n'.format(target_army))
                    print('{0}, out of game'.format(target_army))
                    self.armies_game_over.append(target_army)
        self.armies = list(set(self.armies) - set(self.armies_game_over))
        return self.armies

    def __str__(self):
        return 'Winner:{0}'.format(self.armies[0])
