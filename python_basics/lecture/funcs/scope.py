"""
Scope — это область видимости в Python, которая определяет доступность переменных внутри блока кода.
В Python есть три базовых области видимости переменных:
    • глобальные переменные
    • локальные переменные
    • нелокальные переменные

Переменные, объявленные внутри тела функции, имеют локальную область видимости.
Переменные, объявленные вне тела функции, имеют глобальную область видимости.


Доступ к локальным переменным имеют только те функции, в которых они объявлены.
К глобальным переменным доступ можно получить из любого места программы.
"""

a = 5  #  глобальная переменная

def local():
    a = 7  #  локальная переменная
    print(a)  #  выводим значение локальной переменной


def glob():
    print(a)  #  выводим значение глобальной переменной


local()
glob()
print(a)

"""
Для того, чтобы получить доступ к глобальной переменной, достаточно лишь указать ее имя
Однако если нам надо изменить глобальную переменную внутри функции, мы должны использовать выражение global. 
"""


a = 10  #  глобальная переменная


def glob2():
    global a
    a += 1  #  меняем глобальную переменную


glob2()
print(a)  #  глобальная переменная имеет новое значение


"""
Если при вызове функции мы подставим в качестве значения аргумента переменную, а в теле функции происходит 
изменение аргумента, то изменится значение переданной в качестве аргумента переменной или нет зависит от того, 
с каким типом данных она связана.
"""

def a(b):
    b = 2
    print(b)


c = 3  #  неизменяемый тип данных передаем в функцию
a(c)
print(c)  #  значение не изменилось


def a(b):
    b[0] = 2


c = [3]  #  изменяемый тип данных передаем в функцию
print(c)
a(c)
print(c)  #  значение изменилось



#  нелокальная область видимости

"""
Nonlocal используется во вложенных функциях, когда мы хотим дать интерпретатору понять, что для вложенной функции 
определенная переменная не является локальной, но она и не является глобальной в общем смысле.
"""
def foo():
    name = 'foo'
    print(name)

    def bar():
        nonlocal name  #  обращаемся к переменной name, объявленной во внешней функции
        name = 'bar'  #  меняем значение с 'foo' на 'bar' во внутренней функции, меняем и во внешней

        print(name)

    bar()
    print(name)

foo()

"""
Ключевое слово nonlocal не будет работать с локальными или глобальными переменными и, следовательно, 
должно использоваться для ссылки на переменные в другой области, кроме глобальной и локальной. 
Ключевое слово nonlocal используется во вложенных функциях для ссылки на переменную в родительской функции.
"""