n1 = 0
n2 = 1
x = int(input('Enter number till to print fibonacci sequence : '))

for i in range(x):
    n3 = n2 + n1
    n1 = n2
    n2 = n3
    print(n3)