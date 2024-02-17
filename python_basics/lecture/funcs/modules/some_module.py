#  __all__ не обязательное выражение. В нем указываются сущности, которые будут импортированы
#  с помощью *. То есть from smtg import *

__all__ = (
    'func',
    'func2',
)


def func():
    ...


def func2():
    def func4():
        ...

    func4()
    ...


def func3():
    ...