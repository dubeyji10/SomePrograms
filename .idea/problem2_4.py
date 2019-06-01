import random
def problem2_4():
    A = []
    random.seed(70)
    for i in range(0,10):
        A.append(5*random.random()+30)
    print(A)

problem2_4()