alist = ["a","e","i","o","u","y"]
blist = ["alpha", "beta", "gamma", "delta", "epsilon", "eta", "theta"]

def problem2_2(my_list):
    print(my_list)#0
    print(my_list[0])#1
    print(my_list[-1])#2
    print(my_list[3:5])#3
    print(my_list[0:3])
    print(my_list[3:])#5
    print(len(my_list))#6
    my_list.append("z")#7
    print(my_list)

problem2_2(alist)
problem2_2(blist)
