# spinner_asyncio.py

# credits: Example by Luciano Ramalho inspired by
# Michele Simionato's multiprocessing example
# source:
# http://python-3-patterns-idioms-test.readthedocs.org/en/latest/CoroutinesAndConcurrency.html

import sys
import asyncio

DELAY = 0.1
DISPLAY = '|/-\\'

@asyncio.coroutine
def spinner_func(before='', after=''):
    write, flush = sys.stdout.write, sys.stdout.flush
    while True:
        for char in DISPLAY:
            msg = f'{before} {char} {after}'
            write(msg)
            flush()
            write('\x08' * len(msg))
            try:
                yield from asyncio.sleep(DELAY)
            except asyncio.CancelledError:
                return


@asyncio.coroutine
def long_computation(delay):
    # emulate a long computation
    yield from asyncio.sleep(delay)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    spinner = loop.create_task(spinner_func('Please wait...', 'thinking!'))
    long_task = loop.create_task(long_computation(3))
    long_task.add_done_callback(lambda f: spinner.cancel())
    loop.run_until_complete(spinner)
    loop.close()

