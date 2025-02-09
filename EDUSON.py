#Получение коэффициентов
fjrst_coefficient = int(input('a = ', ))
second_coefficient = int(input('b = ', ))
third_coefficient = int(input('c = ', ))


# Решение по сокращенной формуле, т.к. b - четное
if fjrst_coefficient != 0 and second_coefficient % 2 == 0 and third_coefficient != 0:
    k = second_coefficient / 2
    d1 = k ** 2 - fjrst_coefficient * third_coefficient
    root_1 = (-k + d1 ** 0.5) / fjrst_coefficient
    root_2 = (-k - d1 ** 0.5) / fjrst_coefficient

    print('так как коэффициент b - четное число, решаем по сокращенной формуле')
    print(f'root_1 = {root_1}')
    print(f'root_2 = {root_2}')


# Решение уравнения при с = 0
if fjrst_coefficient != 0 and third_coefficient== 0 and second_coefficient != 0:
    print(f'корень уравнения равен либо нулю, либо {-second_coefficient / fjrst_coefficient}')

# Решение уравнения при b = 0 и c = 0
if fjrst_coefficient != 0 and second_coefficient== 0 and third_coefficient == 0:
    print(f'корни уравнения равны нулю, fjrst_coefficient * x ** 2 = 0')


# Решение полного уравнения
if fjrst_coefficient != 0 and second_coefficient % 2 != 0 and third_coefficient != 0:
    d = second_coefficient ** 2 - 4 * fjrst_coefficient * third_coefficient
    if d > 0:
        root_1 = (-second_coefficient + d ** 0.5) / (2 * fjrst_coefficient)
        root_2 = (-second_coefficient - d ** 0.5) / (2 * fjrst_coefficient)
        print('Так как второй коэффициент - четное число, решаем по сокращенной формуле')
        print(f'Первый корень: {root_1}')
        print(f'Второй корень: {root_2}')
    elif d < 0:
        print(f'так как дискриминант меньше нуля и равен: {d}')
        print('действительных корней нет')
    else:
        k = -second_coefficient / (2 * fjrst_coefficient)
        print(f'уравнение имеет один корень: {k}')


        # Решение уравнения при b = 0
        if fjrst_coefficient != 0 and c != 0 and second_coefficient == 0:
            if (- third_coefficient / fjrst_coefficient) >= 0:
                root_1 = ( -third_coefficient / fjrst_coefficient ) ** 0.5
                print(f'первый корень равен: {root_1}')
                root_2 = (-1) * (( -third_coefficient / fjrst_coefficient ) ** 0.5)
                print(f'второй корень равен: {root_2}')
        if ( - third_coefficient / fjrst_coefficient ) < 0:
            print(f' -third_coefficient / fjrst_coefficient = : {-third_coefficient / fjrst_coefficient},'
                  f' т.е. < 0, поэтому действительных корней нет')