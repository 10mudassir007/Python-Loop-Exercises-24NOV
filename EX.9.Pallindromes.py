list1 = ['level','racer','key','hello','python','radar','banana','elephant']
pallindromes = 0
for words in list1:
    if words[0] == words[-1]:
        pallindromes += 1
print(pallindromes)