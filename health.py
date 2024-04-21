def buy_health(self, health, coins):
    if coins >= 5 and health < 100:
        buy_more = input(f'{self.name}, you have been wounded in battle. Would you like to purchase a healing potion? [Enter yes or no] ')
        if buy_more == 'no':
            print(f'You have decided to continue with {self.health} and carry {self.money} coins. Good luck '
                  f'{self.name}.')
        elif buy_more == 'yes':
            how_many = input(f'Enter the number of potions? ')
            if int(how_many) * 5 > self.money:
                print(f'AH! {self.name}, you do not have enough coins!')
            else:
                potions = int(how_many) * 5
                self.money = coins - potions
                self.health = potions + health
                if self.health >= 100:
                    self.health = 100
                print(f'Power up to restore health...\n')
                print(f'{self.name}, your health is restored to {self.health}.\n You have {self.money} coins '
                      f'remaining.')
        else:
            self.money -= 10
            print(f'Invalid response causes you to trip and loose 10 coins from your stash. You now carry '
                  f'{self.money} coins.')

