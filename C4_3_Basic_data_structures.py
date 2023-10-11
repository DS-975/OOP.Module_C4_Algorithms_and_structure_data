C4.3. Основные структуры данных

Списки: односвязные и двусвязные
После очень тесного знакомства с массивами другие структуры данных будут восприниматься заметно легче, потому что во многом принципы их работы очень схожи.

Сейчас мы перейдем к структуре данных «список». Как уже отмечалось, список как структуру данных стоит отличать от одноименного типа данных в Python. Что называется list (список) в Python — является динамическим массивом. Далее под списком будет пониматься именно «список как структура данных».

Внешне список схож с массивом.

Список — это также упорядоченный набор элементов. Однако, в отличие от массива, который хранится последовательно в одной области памяти, и каждой ячейке линейно соответствует определенный индекс, список может быть хаотично распределен в памяти. Порядок в этой структуре данных задается наличием указателей на следующий (и/или предыдущий) элемент в списке.

img
Источник: www.tvd-home.ru
Если в каждой ячейке памяти хранится указатель только на следующий элемент, то список называется односвязным. Если указатель и на предыдущий и на следующий — имеем двусвязный список. Помимо прочего в ячейке может храниться «индекс» — некоторый порядковый номер объекта в списке. Однако доступ к элементу списка по индексу сильно отличается от аналогичной операции в массиве из-за особенностей хранения. Часто используется хранение в первой ячейке указателя на последний элемент.

Способ хранения списков имеет свои плюсы и минусы.

1
Вставка элемента в конец списка происходит за константное время, если в первой ячейке хранится указатель на последний элемент. Иначе требуется проход по всем элементам до последнего, что потребует O(n) операций. Действительно, мы можем вставить элемент на последнее место, изменив указатель в первой ячейке, чтобы он указывал на новый элемент.

2
Вставка элемента в начало также может быть произведена за константное время, ведь достаточно в новом элементе вставить указатель на тот, что был первым, и дописать указатель на последний элемент.

3
В списке также можно вставить элемент на произвольное место. В отличие от массива, в списках нет необходимости перемещать элементы, однако здесь эту операцию все равно можно сделать асимптотически за O(n) в худшем случае. Дело в том, что для поиска нужного положения нового элемента придется пройтись от первого указателя до необходимого положения в списке. И, например, для вставки элемента на n-1 индекс нужно будет пройти все элементы от 0-го до n-1-го и только после этого производить вставку.

img
Источник: intuit.ru
4
Удаление элемента из начала так же, как и вставка, производится за константное время. Как и в первых двух случаях, нужно всего лишь изменить положение нужных указателей.

5
А вот удаление элемента из произвольного места может занять линейное время. Ответ кроется в том, что нужный элемент требуется найти (по «индексу» или значению) проходом от 0-го до искомого элемента. И даже в случае удаления последнего элемента мы вынуждены пройти весь список, чтобы в первую ячейку записать обновленный указатель на последний элемент. Такой проблемы в двусвязных списках, очевидно, нет.

6
Расширение списка. Благодаря такому способу хранения не требует переносов всей структуры в другую область памяти, как это было в случае динамических массивов, поэтому добавление к первому списку размера n элементов списка размера m потребует только O(m) времени.

7
Общий размер списка может храниться в самой структуре, и тогда его можно узнать за константное время, но это требует дополнительной памяти. Если в конкретной реализации списка не предусмотрено хранение размера, то пересчет элементов займет O(n) операций.

Таким образом можно сказать, что список наиболее удобен, когда нужно обрабатывать элементы в определенном порядке без использования индексации.

Стек (stack)
Рассмотренные нами структуры данных имеют огромные области применения, и благодаря этому появилось несколько надстроек над ними как наиболее частые способы применения.

Сначала приведем «бытовую» аналогию, постепенно приближаясь к абстрактному понятию стека как одной из таких надстроек.

img  Примеры

Вспомним нашу аналогию с ужином. Ужин закончился, тарелки постепенно перемещаются в раковину — одна на другую. Тем самым определяется порядок, в котором эти тарелки будут вымыты, если у вас, конечно, нет желания каждый раз доставать тарелки из середины. Сначала берется верхняя, потом следующая за ней и так дальше, пока тарелки не кончатся. И точно также при подготовке к ужину мы берем стопку чистых тарелок и выставляем их друг за другом. Каждый раз удобнее брать сверху. Принцип схож — есть упорядоченный набор элементов (прямо как массив или список), но производится всегда две операции — взять сверху или положить сверху. Как вы уже наверное догадались — это стек.

img  

Рассмотрим другой пример, более приближенный к computer science. Вспомним рекурсию (она нам еще не раз пригодится в этом модуле).

img
Источник: studfile.net
Пусть у нас есть рекурсивная функция p(n). Мы вызываем ее с аргументом p(5), она вызывает p(4), та, в свою очередь, снова уменьшает аргумент и так до нуля. Однако вычисления будут происходить наоборот! Сначала вычисляется p(0), затем p(1) доходя до самого первого вызова функции.

Задание 4.4.1
Задание на самопроверку.

Убедитесь в этом самостоятельно, написав функцию p(n), вызывающей эту же самую функцию с аргументом, уменьшенным на единицу, и после чего печатающей значение аргумента. Обратите внимание на описанный порядок действий и наличие условие выхода из рекурсии.

Ответ

def p(n):
    if n == 0:
        return
    else:
        p(n-1)
        print(n)
p(5)
# 1
# 2
# 3
# 4
# 5
Здесь мы видим, что сначала выполнились действия последней функции в порядке вызовов, затем предпоследней и т. д., пока не дойдем до первого.

Такой принцип имеет общепринятое название — LIFO — Last In First Out (последний вошел — первый вышел). И именно этот принцип реализует стек.

Иными словами, стек — это структура данных, реализующая LIFO.
img
Источник: infostart.ru
Операции над стеком
Стек может быть реализован как через динамические массивы, так и через списки. Но прежде, чем перейдем к обсуждению конкретной реализации стека, попробуем понять механизмы его работы, а также сложность операций со стеком (куда без них).

1
Вставка элемента в стек (push) 
Работает за O(1), если стек реализован через список и, в среднем, также O(1), если реализован через динамический массив.

2
Удаление верхнего элемента из стека (pop)
Также как и вставка, удаление верхнего элемента происходит за O(1). Действительно, в массиве удаление последнего элемента происходит за константное время, как и в списке, если он двусвязный.

3
Получение значения последнего элемента без удаления (top)
Аналогично предыдущим операциям получение значения последнего элемента происходит за O(1).

4
Общий размер стека (size)
Здесь уже всё зависит от реализации. В случае односвязного списка O(1), если это значение хранится в самой структуре или O(n), если нужен проход по всем элементам для их пересчета. В массиве операция получения размера занимает константное время.

img
Источник: vaseks.me
Задание 4.4.2
1/1 point (graded)
Какую верхнюю границу сложности (худший случай) будет иметь вставка элемента в стек, если он реализован через динамический массив. Необходимо вспомнить особенности расширения массивов.
O(n)
  верно 
Hint
Show answer
Отправить
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.Верно (1/1 балл)Review
Как видно из описания операций, все операции со стеком (как минимум, в среднем) можно сделать за константное время. Этим объясняется столь широкое распространение стека. Его можно эффективно реализовать с помощью типа данных list языка Python. Проведем параллели между операциями над стеком и методами списков.

Задание 4.4.3
1 из 1 балла (оценивается)
 Помощь по управлению с клавиатуры
ЗАДАЧА
Соотнесите операции над стеком и методы типа данных «список» языка Python

An isosceles triangle with three layers of similar height. It is shown upright, so the widest layer is located at the bottom, and the narrowest layer is located at the top.len(list_), зона для перетаскиванияlen(list_)
Элементы, расположенные здесь: Размер стекаlist_[-1], зона для перетаскиванияlist_[-1]
Элементы, расположенные здесь: Получение значения верхнего элементаlist_.pop(), зона для перетаскиванияlist_.pop()
Элементы, расположенные здесь: Удаление верхнего элементаlist_.append(), зона для перетаскиванияlist_.append()
Элементы, расположенные здесь: Вставка элемента наверхМетод list, зона для перетаскиванияМетод list
Элементы, расположенные здесь: Операция над стеком
Отправить

Вернуться К Началу
Сбросить
Показать Ответ
ОБРАТНАЯ СВЯЗЬ
Correctly placed 5 items.

Your highest score is 1.0

Стек является удобным способом представления различных данных, но сейчас мы рассмотрим один пример, который является важным при анализе математических выражений или при анализе кода.

Наверняка вы не раз сталкивались с предупреждением от среды разработки или ошибкой от компилятора, связанной с неправильной расстановкой скобок. Сейчас мы посмотрим, как можно реализовать проверку строки на корректную расстановку скобок с помощью стека.

Примем за корректную расстановку скобок такую, что для каждой открывающей существует закрывающая скобка — такая, что находится на одном «уровне» с ней. Примеры:

()
(()())
(()(()(()())))
Наличие любой открытой, но не закрытой скобки является ошибкой. Ровно как и наличие закрывающей скобки без открывающей.

Напишем функцию par_checker(string), которая проверяет строку string на корректность расстановки скобок.

def par_checker(string):
    stack = []  # инициализируем стек
    
    for s in string:  # читаем строку посимвольно
        if s == "(":  # если открывающая скобка, 
            stack.append(s)  # добавляем ее в стек
        elif s == ")": 
            # если встретилась закрывающая скобка, то проверяем
            # пуст ли стек и является ли верхний элемент - открывающей скобкой
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()  # удаляем из стека
            else:  # иначе завершаем функцию с False
                return False
    # если стек пустой, то незакрытых скобок не осталось
    # значит возвращаем True, иначе - False
    return len(stack) == 0 
Так как функция проверяет вхождение только скобок, то наличие других символов эту функцию не затронет. Убедитесь в этом самостоятельно.

Задание 4.4.4
1/1 point (graded)
Что будет являться результатом работы функции par_checker при следующей входной строке?

(5+6)*(7+8)/(4+3)
True
  верно 
Hint
Show answer
Отправить
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.Верно (1/1 балл)Review
С помощью стека проверять баланс только круглых скобок может показаться слишком затратным. И это действительно так. Однако написанную нами функцию можно расширить для проверки баланса скобок разного рода: круглых, квадратных и фигурных, например.

Задание 4.4.5
Задание на самопроверку.

Модифицируйте функцию проверки баланса скобок для двух видов скобок: круглых и квадратных.

Для реализации такого алгоритма может быть полезным создание словаря, в котором закрывающая скобка — ключ, открывающая — значение.

Ответ
pars = {")" : "(", "]" : "["}

def par_checker_mod(string):
    stack = []
    
    for s in string:
        if s in "([":
            stack.append(s)
        elif s in ")]":
            if len(stack) > 0 and stack[-1] == pars[s]:
                stack.pop()
            else:
                return False
    return len(stack) == 0 
Очередь
Другой вид последовательности, который скорее всего более привычен в бытовом смысле — это очередь.

В отличие от стека он работает по принципу FIFO — First In First Out (первый вошел — первый вышел). Прямо как в любимой всеми очереди к врачу, например.

Очередь может быть реализована как на массивах, так и на списках. В связи с наличием динамического массива в Python (list) попробуем построить очередь, используя эту структуру данных. Она имеет своё ограничение из-за того, что удаление из конца или вставка элемента в начало имеют сложность O(n).

Чтобы обойти это ограничение, зафиксируем несколько свойств очереди:

Определим максимальную длину очереди — N_max.
При переполнении будем запрещать добавление элементов в очередь.
Зафиксируем два указателя:  head (начало) и tail (хвост) очереди.
Закольцуем очередь таким образом, что если указатель tail >= n_max, то мы перемещаем его в начало.
img

По такой схеме может получиться так, что начало очереди в конце списка, а хвост — в его начале.

img
Источник: ermak.cs.nstu.ru
Для очереди можно определить несколько операций:

Вставка элемента в хвост очереди (push).
Получение элемента из начала очереди (top).
Удаление элемента из начала очереди (pop).
Проверка наличия элементов в очереди (is_empty).
Получение размера очереди (size).
Все они выполняются за O(1). И это то, что нужно!

Попробуем создать обработчик задач на бесконечном цикле с использованием очереди:

# Создадим класс Queue - нужная нам очередь
class Queue:
    # Конструктор нашего класса, в нём происходит нужная инициализация объекта
    def __init__(self, max_size):
        self.max_size = max_size  # размер очереди
        self.task_num = 0  # будем хранить сквозной номер задачи

        self.tasks = [0 for _ in range(self.max_size)]  # инициализируем список с нулевыми элементами
        self.head = 0  # указатель на начало очереди
        self.tail = 0  # указатель на элемент следующий за концом очереди
    
    # !!! Класс далее нужно дополнить методами !!!


# Используем класс
size = int(input("Определите размер очереди: "))
q = Queue(size)

while True:
    cmd = input("Введите команду:")
    if cmd == "empty": 
        if q.is_empty():
            print("Очередь пустая")
        else:
            print("В очереди есть задачи")
    elif cmd == "size":
        print("Количество задач в очереди:", q.size())
    elif cmd == "add": 
        if q.size() != q.max_size:
            q.add()
        else:
            print("Очередь переполнена")
    elif cmd == "show": 
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.show()
    elif cmd == "do": 
        if q.is_empty():
            print("Очередь пустая")
        else:
            q.do()
    elif cmd == "exit": 
        for _ in range(q.size()):
            q.do()
        print("Очередь пустая. Завершение работы")
        break
    else:
        print("Введена неверная команда")
Итак, в первую очередь реализуем проверку наличия элементов в очереди.

Задания на самопроверку.

Задание 4.4.6
Добавьте в класс Queue метод is_empty, который проверяет наличие элементов в очереди, используя указатели head и tail. Запрещается использование функции len(list_), так как ее сложность O(n).

Ответ
def is_empty(self):  # очередь пуста?
    # да, если указатели совпадают и в ячейке нет задачи
    return self.head == self.tail and self.tasks[self.head] == 0
Задание 4.4.7
Добавьте в класс Queue метод size, который возвращает текущий размер очереди. Учтите, что необходимо рассмотреть несколько случаев: когда очередь пустая, когда очередь полная (какому условию соответствует?), а также отдельное внимание стоит обратить на тот случай, когда хвост очереди переместился в начало списка (закольцевался).

Ответ
def size(self):  # получаем размер очереди
    if self.is_empty():  # если она пуста
        return 0  # возвращаем ноль
    elif self.head == self.tail:  # иначе, если очередь не пуста, но указатели совпадают
        return self.max_size  # значит очередь заполнена
    elif self.head > self.tail:  # если хвост очереди сместился в начало списка
        return self.max_size - self.head + self.tail
    else:  # или если хвост стоит правее начала
        return self.tail - self.head
Задание 4.4.8
Добавьте в класс Queue метод add, который добавляет задачу в конец очереди. Также учтите, что размер массива ограничен и при достижении этого предела, необходимо перенести указатель в положение 0. После добавления задачи в очередь, она должна вывести уведомление об этом в формате:

"Задача №1 добавлена"
Ответ
def add(self):
    self.task_num += 1  # увеличиваем порядковый номер задачи
    self.tasks[self.tail] = self.task_num  # добавляем его в очередь
    print(f"Задача №{self.tasks[self.tail]} добавлена")

    # увеличиваем указатель на 1 по модулю максимального числа элементов
    # для зацикливания очереди в списке
    self.tail = (self.tail + 1) % self.max_size
Задание 4.4.9
Добавьте в класс Queue метод show, печатающий информацию о приоритетной задаче в формате

"Задача №1 в приоритете"
Ответ
def show(self):  # выводим приоритетную задачу
    print(f"Задача №{self.tasks[self.head]} в приоритете")
Задание 4.4.10
Добавьте в класс Queue метод do, которая печатает в консоль задачу (=выполняет ее) и, соответственно, удаляет ее из очереди, присваивая ей значение 0. Формат вывода:

"Задача №1 выполнена"
Ответ
def do(self):  # выполняем приоритетную задачу
    print(f"Задача №{self.tasks[self.head]} выполнена")
    # после выполнения зануляем элемент по указателю
    self.tasks[self.head] = 0
    # и циклично перемещаем указатель
    self.head = (self.head + 1) % self.max_size
Задание 4.4.11
1/1 point (graded)
Укажите номера задач, которые не успеют выполниться. То есть будут выведены после вызова exit.

Номера вводите через запятую, без пробелов, соблюдая порядок выполнения.

add
add
add
add
do
do
add
add
do
add
do
do
add
add
add
do
exit
7,8,9,10
  верно 
Show answer
Отправить
Some problems have options such as save, reset, hints, or show answer. These options follow the Submit button.Верно (1/1 балл)Review
Вопрос 1: верно