#taking input number
num = int(input('Enter number to find factorial of : '))
result = 1
#using while loop to find the factorial
while num > 0:
    #for example if factorial of 4 then 1 = 1 * 4 until num = 0
    result = result * num
    num = num - 1
print(f'Factorial of given number is {result}')