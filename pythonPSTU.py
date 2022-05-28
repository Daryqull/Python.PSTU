# 1. сумма ряда от 0 - 88888888
n = 88888888
N = n * (n + 1)/2
print(N)

s = sum(range(88888888)) 
print(s)

# 2. Среднее арифметическое ряда
n = [3, 4, 56, 100, 2, 2, 3]
S = sum(n) / 7
print(S)

# 3. Заменить в строке все буквы "х" на "y"
s = 'asdxfghyxyx'
NEW = ''
for c in s:
     if c == 'x' : c = 'y'
     NEW += c
print(NEW)

# 4. Сосчитать произведение чисел кратных и 3 и 5.
n = [3, 4, 56, 100, 15, 2, 20, 30]
ITOG: int = 1
s = 0
for c in (n):
    if n[s] % 3 == 0 and n[s] % 5 == 0:
        ITOG *= n[s]
    s += 1
    print (ITOG)    

n = [3, 4, 56, 100, 15, 2, 20, 30]
m = 1
for c in (n):
    if c % 3 == 0 and c % 5 == 0:
        m = m * c
print (m)       
    
# 5. Заменить в строке все буквы "х" на "y" в исходной строке без ипользования доп. строки.

letters = 'asdxfghyxyx'
print (letters.replace('x', 'y'))
