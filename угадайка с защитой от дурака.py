import random
def guess_num(number = 100):
    num = random.randint(1, number)
    
    print('Угадайте число от 1 до', number)
    count = 1
    while 1:
        n = input()
        while not is_valid(n):
            n = input('Можно вводить только числа от 1 до 100 ')
            is_valid(n)
        n = int(n)
        if n == num:
            print('Вы угадали, поздравляем!')
            print(f'Вам потребовалось {count} попыток')
            if input('Хочешь сыграть еще раз? "д"/"н" ').lower() in ['д', 'l']:
                guess_num()
            else:
                break
        elif n > num:
            print(n, 'Слишком много, попробуйте еще раз: ')
            count += 1
            continue
        else:
            print(n, 'Слишком мало, попробуйте еще раз: ')
            count += 1
            continue
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
def is_valid(n):
    if n.isdigit():
        if 100 >= int(n) >= 1:     
            return True
        else:
            return False
    else:        
        return False
print('Добро пожаловать в числовую угадайку')
number = input('Вы можете ввести правую границу задуманного числа, по умолчанию это 100')
if number.isdigit() and int(number) > 1:
    number = int(number)
    guess_num(number)
else:
    guess_num()
    
    
