def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


element = int(input())
array = [i for i in range(1, 100)]  # 1,2,3,4,...

# запускаем алгоритм на левой и правой границе
print(binary_search(array, element, 0, 99))

array = '1 2 3 6 45 6 1 7 95 4 6 5 1 6 8 9'
# array = '1 2 3 6 45 6 1 7 -95 4 6 5 1 6 8 9'
# array = '1 2 3 6 -45 6 1 7 -95 4 6 5 1 6 8 9'

element = 6
array = list(array.split())

def sort(arr):
    list = []
    for i in arr:
        list.append(int(i))
    list.sort()
    return list

sort_arr = sort(array)

print('Отсортированный массив: ', sort_arr)
print('Длина массива', len(sort_arr))
print('Индекс методом .index():', sort_arr.index(6))

def position_number(array, element, left, right):  # Алгоритм двоичного поиска
    if element > sort_arr[-1]:  # Чтобы убрать IndexError при element>sort_arr[-1] не вызывая исключение
        return 'IndexError'
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        # рекурсивно ищем в левой половине
        return position_number(array, element, left, middle - 1)
    else:  # иначе в правой
        return position_number(array, element, middle + 1, right)


pos_num = position_number(sort_arr, element, 0, len(sort_arr))
print("Индекс алгоритмом двоичного поиска", pos_num)  # индекс искомого