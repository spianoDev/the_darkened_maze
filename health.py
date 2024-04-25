from style import typing

def buy_health(self, health, coins, potion):
    if health == 100:
        typing(f'{self.name}, you are in perfect health. Save your {coins} coins and {potion} potions for the next '
               f'maze!')
        return
    elif potion > 0:
        typing(f'You almost forgot the potion you found in the maze! \n')
        use_potion(self, potion, health)
    elif coins >= 10 and health < 100:
        typing(f'{self.name}, you have been wounded in battle. \n'
                f'A potion would allow you to increase your {health} health. \n'
               f'Each potion will cost 10 coins and you carry {coins}.\n')
        buy_more = input(f'Would you like to purchase a potion? [Enter yes or no] ')
        if buy_more == 'no':
            typing(f'You have decided to continue with {self.health} and carry {self.money} coins. Good luck '
                  f'{self.name}.')
        elif buy_more == 'yes':
            how_many = input(f'Enter the number of potions you would like to purchase. ')
            if int(how_many) * 10 > self.money:
                typing(f'AH! {self.name}, you do not have enough coins!\n')
            else:
                potions = int(how_many) * 5
                self.money = coins - potions
                self.health = potions + health
                if self.health >= 100:
                    self.health = 100
                typing(f'Power up to restore health...\n')
                typing(f'{self.name}, your health is restored to {self.health}.\n You have {self.money} coins '
                      f'remaining.\n')
        else:
            self.money -= 10
            typing(f'Invalid response causes you to trip and loose 10 coins from your stash. You now carry '
                  f'{self.money} coins.\n')
    else:
        use_potion(self, potion, health)
        typing(f'Unfortunately, {self.name}, you only carry {coins} coins and potions are 10 coins each.\n')

def use_potion(self, potion, health):
    while potion > 0:
        use = input(f'{self.name}, you have {potion} potions. Would you like to restore your health? [yes or no] ')
        if use == 'yes':
            self.health += 5
            self.potion = potion - 1
            potion -= 1
        elif use == 'no':
            return
        else:
            self.potion = potion - 1
            potion -= 1
            typing(f'Invalid response causes you to lose your grip on the potion, smashing it on the hard '
                   f'ground. \n'
                   f'You now carry {self.potion} potions.\n')
            continue
    buy_health(self, self.potion, self.money, health)
