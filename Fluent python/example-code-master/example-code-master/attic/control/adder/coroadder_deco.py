"""

    >>> adder = adder_coro()
    >>> next(adder)
    0
    >>> adder.send(10)
    10
    >>> adder.send(20)
    30
    >>> adder.send(30)
    60
    >>> try:
    ...     next(adder)
    ... except StopIteration as exc:
    ...     result = exc.value
    ...
    >>> result
    Result(sum=60, terms=3, average=20.0)


Closing a coroutine:

    >>> adder = adder_coro()
    >>> next(adder)
    0
    >>> adder.send(1)
    1
    >>> adder.send(10)
    11
    >>> adder.close()
    >>> try:
    ...     next(adder)
    ... except StopIteration as exc:
    ...     exc.value is None
    ...
    True

"""

import sys
import collections


def coroutine(func):
    def primed_coroutine(*args, **kwargs):
        coro = func(*args, **kwargs)
        next(coro)
        return coro
    return primed_coroutine


Result = collections.namedtuple('Result', 'sum terms average')


@coroutine
def adder_coro(initial=0):
    total = initial
    num_terms = 0
    while True:
        try:
            term = yield total
        except GeneratorExit:
            break
        if term is None:
            break
        total += term
        num_terms += 1
    return Result(total, num_terms, total/num_terms)


def prompt():
    while True:
        try:
            term = float(input('+ '))
        except ValueError:
            break
        yield term


def main(get_terms):
    adder = adder_coro()
    for term in get_terms:
        adder.send(term)
    try:
        adder.send(None)
    except StopIteration as exc:
        result = exc.value
    print(result)


if __name__ == '__main__':
    get_terms = (float(n) for n in sys.argv[1:]) if len(sys.argv) > 1 else prompt()
    main(get_terms)
