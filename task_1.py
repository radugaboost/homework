def search_big_str(s):
    mini_letters = 0
    big_letters = 0
    for letter in s:
        if letter.islower():
            mini_letters += 1
        else:
            big_letters += 1
    return big_letters > mini_letters

strings = str(input("Введите строку: ")).split()
big_str = 0
small_str = 0

for string in strings:
    if search_big_str(string):
        big_str+=1
    else:
        small_str+=1

result = (big_str / (small_str + big_str)) * 100
    
print(result)