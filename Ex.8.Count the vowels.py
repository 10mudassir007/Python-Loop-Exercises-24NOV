#String is given
string = 'Programming Fundamentals'
#Vowels in upper and lower case
vowels = 'aeiouAEIOU' 
#predefining number of vowels
num_of_vowels = 0
#using for loop for checking each letter in string and vowels and counting those which are in both, in other words which are vowels
for letters in string:
    if letters in vowels:
        num_of_vowels += 1
#printing the number of vowels
print(num_of_vowels)
