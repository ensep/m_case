import asyncio
import math


def find_duplicate_array(items):
    return set([item for item in items if items.count(item) > 1])


arr = find_duplicate_array(['2', '3', '4', '4', '4', '5', '5'])

open_brackets = ['{', '(', '[']
close_brackets = ['}', ')', ']']


def check_brackets(my_string):
    brackets = []
    for v in my_string:
        if v in open_brackets:
            brackets.append(v)
        elif v in close_brackets:
            close_index = close_brackets.index(v)
            if len(brackets) > 0 and \
                    open_brackets[close_index] == brackets[len(brackets) - 1]:
                brackets.pop()
            else:
                return False
    return len(brackets) == 0


test = '{[]}'
print(check_brackets(test))
test = '{[}'
print(check_brackets(test))
test = '{}'
print(check_brackets(test))


array_list = ['a', 'b', 'c', 'd']


async def async_function():
    for i, v in enumerate(array_list):
        second = int(math.pow(2, i))
        await asyncio.sleep(second)
        print('printed %s second..' % second)
        print(v)

asyncio.run(async_function())
