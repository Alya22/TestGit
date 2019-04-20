
while True:
    try:
        import numpy as np; import random
        n = 7
        A = np.zeros(n,dtype=np.int_)
        for i in range(n):
            A[i] = random.randint(0,20)
        print("Исходный массив",A)
        print("Резельтат:",A*2)
        print("\nВы хотите продолжить работу?")
        d = input('\nЕсли да введите 1,если нет введите любой символ: ')
    except (ValueError, TypeError, IndexError):
        print("Вы ввели неверное значение!Попробуйте еще раз!")
    else:
        if d == '1':
            print("Вы начали выполнение программы сначала")
            continue
        else:
            print("Программа завершена.")
        break