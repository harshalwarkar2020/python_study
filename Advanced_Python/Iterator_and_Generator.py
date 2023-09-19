"""
Iterable:-
- An Iterable is an object which is capable of returning its members one by one.
- In iterable _iter_() or __get item__ methods are defined.
- __iter__() method is used to get an iterator.
- List, dictionaries, string, tuple and sets are all iterable objects.

Iterators:-
 - an iterator is an object that can be iterated upon, meaning that we can traverse
   through all the values.

Iteration:-
- The process of iteration is called iteration.
"""

x = "harry"
y = iter(x)

print(y.__next__())
print(y.__next__())

print("------------------------------------------------------------------------------------------")
"""Generator In Python:-
- Generators are kind of iterators.
- They are kind of iterators which we are iterating once only.
- It is defined like a normal function, but yield keyword used to generate the value instead of
  return.
- return will terminate the function but yield does not terminate the function.
- If the body of def contains yield, then that function automatically becomes a generator
  function.
"""


def gen_one():
    yield 1
    yield 20
    yield 40


value = gen_one()
print(value.__next__())
print(value.__next__())
print(value.__next__())
print("------------------------------------")


def gen_two():
    yield 1000
    yield 2000
    yield 4000


value = gen_two()
for i in value:
    print(i)
print("------------------------------------")


def gen_three(n):
    for i in range(n):
        yield i


value = gen_three(4)
print(value.__next__())
print(value.__next__())
print("------------------------------------")
