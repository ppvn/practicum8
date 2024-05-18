while True:
    num = input('Введите число: ')
    if num.isdigit():
        num_int = int(num)
        print('Введено целое число:', num_int)
        break
    else:
        print('Ошибка. Попробуйте еще раз. Введите целое число.')