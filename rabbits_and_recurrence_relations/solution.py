

def fib(n, k):
    previous1, previous2 = 1, 1
    for i in range(2, n):
        current = previous1 + k * previous2
        previous2 = previous1
        previous1 = current
    return current

print(fib(33,4))

#3048504677680
#The total number of rabbit pairs pressent after n months if each generation of reproduction age rabbits
#produces a litter of k rabbit pairs