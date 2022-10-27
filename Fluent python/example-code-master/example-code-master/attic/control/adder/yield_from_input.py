import sys


def ask():
    prompt = '>'
    while True:
        if response := input(prompt):
            yield response
        else:
            return 0


def parse_args():
    yield from iter(sys.argv[1:])


def fetch(producer):
    gen = producer()
    next(gen)
    yield from gen


def main(args):
    producer = parse_args if args else ask
    total = 0
    count = 0
    gen = fetch(producer())
    while True:
        term = yield from gen
        term = float(term)
        total += term
        count += 1
        average = total / count
        print(f'total: {total}  average: {average}')


if __name__ == '__main__':
    main(sys.argv[1:])
