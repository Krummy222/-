import random
def text(s):
    while 1:
        if s.isdigit():
            s = int(s)
            return s
        else:
            s = input('нужно число, если не нужно то "0": ')
def password(n, m, q, r, long):
    password = []
    for _ in range(n): # добавляем маленькие буквы
        password += [chr(random.randint(97, 122))]
    for _ in range(m): # добавляем большие буквы
        password += [chr(random.randint(65, 90))]
    for _ in range(q): # добавляет спецсимволы
        password += [random.choice(['@', '#', '$', '%', '!'])]
    for _ in range(r): # добавляем цифры
        password += [random.randint(0, 9)]
    while len(password) < long: #добиваем рандомом
        ran = random.choice(test)
        if ran == 1:
            password += [chr(random.randint(97, 122))]
        elif ran == 2:
            password += [chr(random.randint(65, 90))]
        elif ran == 3:
            password += [random.choice(['@', '#', '$', '%', '!'])]
        else:
            password += [random.randint(0, 9)]
    random.shuffle(password)  #взбалтываем 
    return password   
def many_pass(many):
    for _ in range(many):
        print(*password(n, m, q, r, long), sep = '')
test = []        
long = input('Введите необходимую длинну пароля ')
long = text(long)
n = input('Введите количество маленьких букв необходимых для пароля, или "0" если они не нужны: ')
n = text(n)
if n > 0:
    test += [1]
m = input('Введите количество больших букв необходимых для пароля, или "0" если они не нужны: ')
m = text(m)
if m > 0:
    test += [2]
q = input('Введите количество спецсимволов необходимых для пароля, или "0" если они не нужны: ')
q = text(q)
if q > 0:
    test += [3]
r = input('Введите количество цифр необходимых для пароля, или "0" если они не нужны: ')
r = text(r)
if q > 0:
    test += [4]
many = input('Сколько таких паролей нужно сгенерировать? ')
many = text(many)            
many_pass(many)

