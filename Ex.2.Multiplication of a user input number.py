#using for loop to print first 10 numbers
num = int(input('Enter number to create multiplication table of : '))
for i in range(1,11):
    #printing the numbers
    print(f'{num} x {i} = {num * i}')
