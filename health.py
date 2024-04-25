from style import typing

def buy_health(self, health, coins, potion):
    typing(f'Before continuing to the next level, you have the option to restore your health.')
    if health == 100:
        typing(f'{self.name}, you are in perfect health. Save your {coins} coins and {potion} potions for the next '
               f'maze!')
    if coins >= 10 and health < 100:
        buy_more = input(f'{self.name}, you have been wounded in battle. Would you like to purchase a healing potion? [Enter yes or no] ')
        if buy_more == 'no':
            typing(f'You have decided to continue with {self.health} and carry {self.money} coins. Good luck '
                  f'{self.name}.')
        elif buy_more == 'yes':
            how_many = input(f'Enter the number of potions? ')
            if int(how_many) * 10 > self.money:
                typing(f'AH! {self.name}, you do not have enough coins!')
            else:
                potions = int(how_many) * 10
                self.money = coins - potions
                self.health = potions + health
                if self.health >= 100:
                    self.health = 100
                typing(f'Power up to restore health...\n')
                typing(f'{self.name}, your health is restored to {self.health}.\n You have {self.money} coins '
                      f'remaining.')
        else:
            self.money -= 10
            typing(f'Invalid response causes you to trip and loose 10 coins from your stash. You now carry '
                  f'{self.money} coins.')

def use_potion(self, potion, health):
    while potion > 0:
        use = input(f'{self.name}, you have {potion} potions. Would you like to restore your health? [yes or no] ')
        if use == 'yes':
            self.health = potion * 10 + health
            potion = self.potion - 1
        elif use == 'no':
            return
        else:
            potion = self.potion - 1
            typing(f'Invalid response causes you to lose your grip on the potion, smashing it on the hard '
                   f'ground. '
                   f'You now carry {self.potion} potions.')
