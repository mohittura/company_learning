import random 
# for i in range(3):
#     print(random.randint(10,20))
#     print(random.random())

# members = ["Mohit", "Neel", "Harsh", "Jay"]

# print(random.choice(members))


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return first, second
    
dice = Dice()
print(dice.roll())