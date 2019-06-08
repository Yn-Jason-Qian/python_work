from random import randint

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self, time):
        count = 0
        while count < time:
            print(str(randint(1, self.sides)))
            count+=1

die6 = Die(6)
die6.roll_die(10)

print("die6 roll over.")

die10 = Die(10)
die10.roll_die(10)
print("die10 roll over.")

die20 = Die(20)
die20.roll_die(10)
print("die20 roll over.")
