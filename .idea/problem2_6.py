import random
def problem2_6():
    random.seed(431)
    for roll in range(0,100):
        diceA = random.randint(1,6)
        diceB = random.randint(1,6)
        print(diceA+diceB)
problem2_6()