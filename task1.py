# Задание:
# Дано: матрица 10*10*10, заполненная случайными числами [0;9].
# Найти: три взаимно перпендикулярных столбца, сумма чисел в которых будет максимальной.

import numpy as np

# данные по умолчанию
matrix_size = (10, 10, 10)
min_value = 0
max_value = 9

# создаем массив размером MATRIX_SIZE, который будет заполняться
# случайными целыми числами от MIN_VALUE до MAX_VALUE
array = np.random.randint(min_value, max_value, matrix_size)

sum_max = 0
coordinates_array = []

# Пройдемся по всем елементам массива и найдем для кажкого из елементов
# сумму столбцов, которые пересекаются на этом елементе (то есть они взаимно перпендикурярны)
# Если сумма для некоторого елемента окажеться больше чем максимальная
# сумма для предыдущих елементов, заменим максимальну сумму на текущую
# Если суммы равны добавим координаты текущего елемента в список елементов
# с максимальной суммой, что бы показать, что таких максимальных пересечений
# может быть несколько
for matrix in range(matrix_size[0]):
    for row in range(matrix_size[1]):
        for column in range(matrix_size[2]):
            element = array[matrix][row][column]
            coordinates = (matrix, row, column)
            
            sum_x = sum(array[matrix][row])
            sum_y = sum(array[matrix])[column]
            sum_z = sum(array)[row][column]

            sum_current = sum_x + sum_y + sum_z - element*2

            if sum_max < sum_current:
                sum_max = sum_current
                coordinates_array = [coordinates]
            elif sum_max == sum_current:
                coordinates_array.append(coordinates)

print("Max sum is: ", sum_max)
print("For element(s) with coordinates : ", *coordinates_array)

answer = input("Show array ? (Y/N) ")
if answer.lower() == 'y':
    print(array)

input("Press any key to finish")