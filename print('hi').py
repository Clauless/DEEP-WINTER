#=========< 다음 AwesomeDice 클래스를 완성하세요 >==========
import random

class AwesomeDice:
    def __init__(self,n):
        self.n = n

        list1=[]
        k=1
        for i in range(1,n+1):
            if len(list1)<n:
                for j in range(1,k+1):
                    if len(list1)<n:
                        list1.append(k)
            k+=1
        
        self.dice = list1
        

    def roll_dice_once(self):
        return random.choice(self.dice)

    def roll_dice_until_get_max (self):
        count = 0
        while True:
            count += 1
            if self.roll_dice_once() == max(self.dice):
                return count
        return count

    def __str__(self):
        return str(self.dice)

target_dice = AwesomeDice(144)
print(target_dice.roll_dice_once())

roll_count = 0
for i in range(30):
    roll_count += target_dice.roll_dice_until_get_max()
print(roll_count / 30)

print(target_dice)