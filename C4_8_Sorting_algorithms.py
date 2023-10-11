# C4.8. Алгоритмы сортировки
#
# Перейти к основному содержимому
# img
#
# За плечами огромный опыт работы со структурами данных и уже с некоторыми алгоритмами. Напоследок рассмотрим последнюю тему, имеющую огромное значение при работе с линейными структурами данных — сортировка.
#
# Данные, которые приходят в программу из внешней среды, чаще всего являются несортированными — их порядок ничем не определяется. Однако согласитесь, что это далеко не всегда удобно. А если мы говорим про алгоритмы, то это еще и сильно снижает эффективность.
#
# В заключительной части модуля мы рассмотрим некоторые алгоритмы сортировки:
#
# Наивная сортировка (чтобы показать, как делать не стоит).
# Сортировка выбором (чуть менее наивный, но далек от идеала).
# Сортировка пузырьком (пожалуй, самый понятный в реализации, но далеко не самый эффективный).
# Сортировка вставками (неплохо).
# Сортировка слиянием (заметно лучше).
# Быстрая сортировка (почти идеально!).
# Наивная сортировка
# Мы показываем наивную сортировку, чтобы показать, как делать не нужно ни в коем случае!
#
# Ее основная суть заключается в том, чтобы постоянно перемешивать массив, пока не получим подходящую последовательность… Звучит очень долго с точки зрения времени выполнения. И это правда так, ведь для массива из n элементов нам нужно сделать n! (факториал) перестановок и проверить каждую из них. Помните, в начале модуля мы говорили про алгоритмы сложности O(n!). Сейчас в первый и в последний раз, мы с вами реализуем такой алгоритм.
#
# import random  # модуль, с помощью которого перемешиваем массив
#
# # пусть имеем массив всего лишь из 9 элементов
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# is_sort = False  # станет True, если отсортирован
# count = 0  # счетчик количества перестановок
#
# while not is_sort:  # пока не отсортирован
#     count += 1  # прибавляем 1 к счетчику
#
#     random.shuffle(array)  # перемешиваем массив
#
#     # проверяем отсортирован ли
#     is_sort = True
#     for i in range(len(array)-1):
#         if array[i] > array[i+1]:
#             is_sort = False
#             break
#
# print(array)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(count)
# # 290698
# Уже для 9 элементов получили какое-то нереальное число. Невозможно представить, что будет, если в массиве будет хотя бы 100 элементов.
#
# Задание 4.8.1
# 1/1 point (graded)
# Найдите количество цифр в записи числа 100! (факториал от 100).
# 158
#   верно
#
# Show answer
# Отправить
# Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.Верно (1/1 балл)Review
# Надеюсь, теперь понятно, почему так делать не стоит.
#
# Сортировка выбором
# Допустим, намотали на ус, что перестановками нам ничего хорошего не добиться.
#
# Следующее решение «в лоб» — каждый раз искать минимальный элемент и ставить его в начало. Звучит уже интереснее.
#
# img
# Источник: pythonist.ru
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
# for i in range(len(array)): # проходим по всему массиву
#
#         idx_min = i # сохраняем индекс предположительно минимального элемента
#         for j in range(i+1, len(array)):
#                 if array[j] < array[idx_min]:
#                         idx_min = j
#         if i != idx_min: # если индекс не совпадает с минимальным, меняем
#                 array[i], array[idx_min] = array[idx_min], array[i]
#
# print(array)
# На каждом шаге мы имеем отсортированную (слева) и неотсортированную часть (справа). Ищется минимальный элемент в неотсортированной части и меняется местами с элементом в начале неотсортированной части. И так продолжается, пока не закончится внешний цикл.
#
# Задание 4.8.2
# 1/1 point (graded)
# Посчитайте количество сравнений элементов списка, которые производятся в алгоритме выбором из примера.
# 36
#   верно
#
# Show answer
# Отправить
# Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.Верно (1/1 балл)Review
# Задание 4.8.3
# Задание на самопроверку.
#
# Модифицируйте описанный алгоритм для сортировки по убыванию.
#
# Ответ
# for i in range(len(array)):
#     idx_max = i
#     for j in range(i, len(array)):
#         if array[j] > array[idx_max]:
#             idx_max = j
#     if i != idx_max:
#         array[i], array[idx_max] = array[idx_max], array[i]
#    Дополнительный материал
# Сортировка выбором в виде танца.
# Сортировка пузырьком
# img
#
# Сортировка пузырьком — самый любимый студентами вид сортировки. Его суть сводится к тому, что максимальные элементы шаг за шагом «всплывают» вправо — в отсортированную часть массива. И по ходу совершаются еще перестановки, если это необходимо, ведь каждый раз мы сравниваем только соседние элементы!
#
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#
# for i in range(len(array)):
#     for j in range(len(array)-i-1):
#         if array[j] > array[j+1]:
#             array[j], array[j+1] = array[j+1], array[j]
#
# print(array)
# Алгоритм сортировки как пузырьком, так и выбором, имеет среднюю сложность O(n^2), потому что мы имеем два вложенных цикла, каждый из которых, в среднем, проходится по половине всего количества элементов. На первой итерации проверяется N-1 условие, на второй N-2 и т. д., пока на последней итерации не останется только 1 условие (сравнить первый и второй элементы). Можно убедиться, что среднее количество будет равно ~N/2 на каждой итерации, которых N. Это и приводит нас к квадратичной сложности обоих алгоритмов. Однако пузырек все-таки побеждает, потому что на каждую итерацию тратиться чуть-чуть меньше времени.
#
# Пузырек удобен, когда структура имеет не очень большой размер и очень важна скорость написания кода. В таком случае пузырек идеален — два цикла, одно условие и один swap (перестановка двух элементов). Однако на более крупных массивах пузырек сильно проигрывает другим алгоритмам.
#
#   Дополнительный материал
# Сортировка пузырьком в виде танца.
# Сортировка вставками
# img
# Источник: ru.wikipedia.org
# Готовы сами написать сортировку? Никаких сомнений — готовы! Что должен сделать алгоритм?
#
# В начале итерации устанавливается ведущий элемент. На первой итерации — самый первый элемент и по умолчанию он считается уже отсортированным.
# Сохраняем ведущий элемент в дополнительную переменную (красный квадрат в анимации).
# Далее происходит поиск места, куда должен встать ведущий элемент в уже отсортированной (левой) части массива. Можно, например, использовать цикл while с условием достижения границы и/или успешным нахождением элемента. Пока условие цикла выполняется происходит сдвиг каждого элемента вправо.
# По завершении цикла сохраненное значение переменной помещается на освободившееся место. Алгоритм завершается.
#   Дополнительный материал
# Сортировка вставками в виде танца.
# Задание 4.8.4
# Задание на самопроверку.
#
# Реализуйте алгоритм сортировки вставками.
#
# Ответ
# for i in range(1, len(array)):
#     x = array[i]
#     idx = i
#     while idx > 0 and array[idx-1] > x:
#         array[idx] = array[idx-1]
#         idx -= 1
#     array[idx] = x
# Задание 4.8.5
# 1/1 point (graded)
# Вам нужно вставить строку count += 1 так, чтобы код считал количество сравнений элементов списка. В ответе напишите, чему равно количество сравнений элементов списка, которые производятся в алгоритме сортировки вставками.
#   count = 0
#
# array = [2, 3, 1, 4, 6, 5, 9, 8, 7]
#   for i in range(1, len(array)):
#       x = array[i]
#       idx = i
#       while idx > 0:
#           if (array[idx-1] <= x):
#               break
#           array[idx] = array[idx-1]
#           idx -= 1
#       array[idx] = x
#
# print(count)
# 13
#   верно
#
# Show answer
# Отправить
# Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.Верно (1/1 балл)Review
# Сравните результаты. Алгоритм сортировки вставками хоть и является также квадратичным по времени (в среднем), но имеет меньшие множители (в силу уменьшенного количества тяжелых операций). И к тому же очень хорошо работает на почти отсортированных массивах.
#
# Сортировка слиянием
# img
#
# Сортировка слиянием основана на принципе «разделяй и властвуй». Без шуток. Сначала делим массив пополам (или почти пополам, если в массиве нечетное количество элементов). И снова пополам. И снова. Еще раз. Пока не устанете. Ладно, на самом деле программа сама это сделает, если использовать рекурсию. А выход из рекурсии случится тогда, когда отделенный кусок массива станет размером 1, т. е. сократится до одного элемента. А один элемент уж точно можно считать отсортированным относительно себя. Полпути сортировки можно считать пройденной.
#
# Дальше — интереснее.
#
# Нам нужно склеивать обратно расщепленные части массива, потому она и называется сортировкой слиянием. Итак, имеем два одиночных элемента — сравниваем их и возвращаем на предыдущий уровень рекурсии в нужном порядке.
#
# Когда имеем больше элементов в каждой из частей, подлежащих слиянию, нужно быть предельно аккуратным:
#
# Сравниваем первые элементы.
# В результирующий массив записываем наименьший.
# Сравниваем первый элемент в нетронутом и второй элемент из другой части.
# Сравниваем — склеиваем в результат.
# И так продолжается, пока не будет достигнут конец одной из частей.
# Последний штрих — в результирующий массив записать все элементы из еще пока непустой части.
# Вернуть результат на предыдущий уровень рекурсии.
#   Дополнительный материал
# Сортировка слиянием в виде танца.
# Задание 4.8.6
# Задание на самопроверку.
#
# Реализуйте алгоритм сортировки слиянием.
#
# Ответ
# def merge_sort(L):  # «разделяй»
#     if len(L) < 2:  # если кусок массива равен 2,
#         return L[:]  # выходим из рекурсии
#     else:
#         middle = len(L) // 2  # ищем середину
#         left = merge_sort(L[:middle])  # рекурсивно делим левую часть
#         right = merge_sort(L[middle:])  # и правую
#         return merge(left, right)  # выполняем слияние
#
# def merge(left, right):  # «властвуй»
#     result = []  # результирующий массив
#     i,j = 0,0  # указатели на элементы
#
#     # пока указатели не вышли за границы
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     # добавляем хвосты
#     while i < len(left):
#         result.append(left[i])
#         i += 1
#
#     while j < len(right):
#         result.append(right[j])
#         j += 1
#
#     return result
# Это один из вариантов сортировки слиянием. Давайте подумаем, какая у него будет сложность. При слиянии мы сравниваем элементы друг с другом, но количество сравнений будет не очень большим, ведь мы склеиваем уже сортированные части массива. А вот операция деления схожа с тем, что мы делали с деревьями. Если каждый раз делим пополам, то для структуры из n элементов имеем сложность ~O(log(n)). Умножая сложности друг на друга, имеем общую сложность O(n*log(n)). И это круто!
#
# Однако написанный нами алгоритм требует много дополнительной памяти, чтобы хранить промежуточные части массива. Решению этой проблемы посвящено много исследований.
#
# В частности можно ознакомиться со следующей статьей, которая на простых словах объясняет различные нюансы, связанные с выделением памяти.
#
# Быстрая сортировка
# img
# Источник: algolab.valemak.com
# Быстрая сортировка так же, как и сортировка слиянием, является одной из самых быстрых. Она так же основана на принципе «разделяй и властвуй». Однако вместо разделения массивов на части и дальнейшего слияния здесь используется другой подход.
#
# Алгоритм выполняется рекурсивно следующим образом:
#
# Выбирается ведущий элемент (есть несколько вариантов, о которых поговорим чуть позже).
# Две части массива сортируются только на основе этого ведущего элемента.
# Происходит последовательный обмен значениями элементов. Вопрос в том, какие элементы обменивать. Сначала происходит поиск слева направо до первого элемента, который превосходит по своему значению ведущий элемент. Затем массив просматривается справа налево в поисках элемента, который меньше ведущего. Когда такие элементы найдены, происходит их обмен.
# Таким образом, в левой части массива имеются элементы только меньше ведущего, а в правой — только больше.
# Функция рекурсивно применяется к получившимся частям массива, если их размеры превосходят один элемент.
#   Дополнительный материал
# Быстрая сортировка в виде танца.
# def qsort(array, left, right):
#     middle = (left+right) // 2
#
#     p = array[middle]
#     i,j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort(array, left, j)
#     if right > i:
#         qsort(array, i, right)
# Быстрая сортировка хоть и быстрая, но не всегда. В среднем она работает, как и сортировка слиянием, за O(n*log(n)). Однако существуют некоторые экстремальные случаи, на которых быстрая сортировка начинает работать намного хуже. Такое происходит, если на каждой итерации выбирается минимальный (максимальный) элемент структуры. И тогда размер одной из частей массива всегда равен 1, а размер другой — N-1. И тогда по сложности быстрая сортировка становится не лучше, чем сортировка пузырьком. И это не то, что мы ожидали.
#
# Для того, чтобы обойти это ограничение, пользуются некоторыми хитростями. Стоит сказать, что вообще-то ведущий элемент сам по себе не обязан принадлежать массиву. Главное, что от него требуется — разделить массив на как можно более близкие по размеру части.
#
# Поэтому существует несколько способов улучшить работу быстрой сортировки, чтобы даже в худшем случае не доводить затраты по времени до O(n^2):
#
# Нахождение среднего между первым и последним элементом массива.
# Нахождение медианы между первым, средним и последним элементами.
# Наиболее оптимально находить медиану всей последовательности, но это может быть слишком затратно.
# Рандомный элемент.
# Как правило, на практике в качестве ведущего элемента выбирается случайно выбранный из всей последовательности.
# Благодаря такому выбору вероятность попасть на минимальный (максимальный) элемент достаточно быстро стремится к нулю,
# что особенно справедливо на очень больших массивах.
#
# Задание 4.8.7
# Задание на самопроверку.
#
# Модифицируйте алгоритм быстрой сортировки таким образом, чтобы ведущий элемент выбирался как случайный среди
# подмассива, который сортируется на данном этапе. Воспользуйтесь функцией из пакета random.
#
# import random
#
# # random.choice(array[idx_left: idx_right])
# Ответ
# def qsort_random(array, left, right):
#     p = random.choice(array[left:right+1])
#     i, j = left, right
#     while i <= j:
#         while array[i] < p:
#             i += 1
#         while array[j] > p:
#             j -= 1
#         if i <= j:
#             count += 1
#             array[i], array[j] = array[j], array[i]
#             i += 1
#             j -= 1
#
#     if j > left:
#         qsort_random(array, left, j)
#     if right > i:
#         qsort_random(array, i, right)
# Итоги
# Подведем итоги рассмотрения алгоритмов сортировок.
#
# Естественно, это далеко не все существующие алгоритмы сортировки. Нами остались не затронуты:
#
# Сортировка кучей.
# Эта сортировка основана на построении двоичного дерева, обладающего некоторыми свойствами.
# Сортировка Шелла.
# Плавная сортировка.
# Интересная сортировка, основанная на числах Леонардо, которые похожи на числа Фибоначчи.
# Timsort. Обратите на нее особое внимание, потому что именно эта сортировка используется во встроенных сортировках языка Python. Она заслуживает рассмотрения, поскольку учитывает еще и эмпирические факты.
#
#
# Алгоритм	Временная сложность	Пространственная сложность
# Лучший	Средний	Худший	Худший
# Сортировка выбором	O(n^2)	O(n^2)	O(n^2)	O(1)
# Сортировка пузырьком	O(n)	O(n^2)	O(n^2)	O(1)
# Сортировка вставками	O(n)	O(n^2)	O(n^2)	O(1)
# Сортировка слиянием	O(n*log(n))	O(n*log(n))	O(n*log(n))	O(n)
# Быстрая сортировка	O(n*log(n))	O(n*log(n))	O(n^2)	O(log(n))
# img
#
# Если вы хотите углубиться в изучение алгоритмов и структур данных, приглашаем вас на микро-курс
# «Алгоритмы и структуры данных. PRO».
#
# Курс подойдет для разработчиков, хорошо владеющих языками Java/C++/Python и желающих продолжить прокачивать алгоритмическое мышление, решая задачки.
# Ознакомиться с программой курса и оставить заявку вы можете здесь.
#
# Для студентов наших курсов скидка 3000 р. по промокоду ALGO3000.
#
# Вопрос 1: верно

