
sequence_of_numbers = input('Введите целые числа через пробел: ')
user_number = int(input('Введите любое число: '))

error = 'Пожалуйста перезапустите программу'

# Определяем цифры в строке:
def is_int(str):
    str = str.replace(' ', '')
    try:
        int(str)
        return True
    except ValueError:
        return False

# Проверка на соответствие условиям ввода:
if " " not in sequence_of_numbers:
    print("\n Вы ввели числа без пробелов (повторите ввод согласно условиям!)")
    sequence_of_numbers = input('Введите целые числа через пробел: ')
if not is_int(sequence_of_numbers):
    print('\n Были введены числа отличные от целых, либо не цифры (введите числа, согласно условиям ввода.)\n')
    print(error)
else:
    sequence_of_numbers = sequence_of_numbers.split()

# Преобразование списка строк в список чисел:
list_sequence_of_numbers = [int(item) for item in sequence_of_numbers]

# Сортировка списка
def merge_sort(L):
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) // 2
        left = merge_sort(L[:middle])
        right = merge_sort(L[middle:])
        return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
    return result

list_sequence_of_numbers = merge_sort(list_sequence_of_numbers)

# Установка позиции элемента:
def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите пожалуйста меньшее число.'

# Установка номера позиции элемента, который меньше введенного пользователем числа,
# следующий за ним больше или равен этому числу:

print(f'Список упорядоченный по возрастанию: {list_sequence_of_numbers}')

if not binary_search(list_sequence_of_numbers, user_number, 0, len(list_sequence_of_numbers)):
    rI = min(list_sequence_of_numbers, key=lambda x: (abs(x - user_number), x))
    ind = list_sequence_of_numbers.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_number:
        print(f'''В списке отсутствует введенный элемент 
Ближайший наименьший элемент: {rI}, с индексом: {ind}
Ближайший наибольший элемент: {list_sequence_of_numbers[max_ind]} с индексом: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке отсутствует введенный элемент 
Ближайший элемент больший по значению: {rI}, с индексом: {list_sequence_of_numbers.index(rI)}
Список не содержит меньший элемент''')
    elif rI > user_number:
        print(f'''В списке нет элемента совпадающего с введенным по значению.
Ближайший элемент больший по значению: {rI}, с индексом: {list_sequence_of_numbers.index(rI)}
Ближайший элемент меньший по значению: {list_sequence_of_numbers[min_ind]} с индексом: {min_ind}''')
    elif list_sequence_of_numbers.index(rI) == 0:
        print(f'Индекс введенного элемента: {list_sequence_of_numbers.index(rI)}')
else:
    print(f'Индекс введенного элемента: '
          f'{binary_search(list_sequence_of_numbers, user_number, 0, len(list_sequence_of_numbers))}')

input()



 ###
#A.sort()
#print('Введите любое число:')
#user_number = input()
#print('Введите числа через пробел:')
#A = input().split()

#преобразование в список
#for i in range(len(A)):
#    A[i] = int(A[i])
#print(A)

#Сортировка списка по возрастанию элементов в нем

#def Sort_list_by_age():
#    for i in range(1, len(A)):
#        x = A[i]
#        idx = i
#        while idx > 0 and A[idx - 1] > x:
#            A[idx] = A[idx - 1]
#            idx -= 1
#        A[idx] = x

#Sort_list_by_age()

#print(A)

