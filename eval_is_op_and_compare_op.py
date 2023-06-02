import dis
import timeit
import datetime
from faker import Faker

fake = Faker()

def is_none(x):
    return x is not None

def is_equal_none(x):
    return x != None

integers = [fake.random_int() for _ in range(10000)]
datetimes = [fake.date_time() for _ in range(10000)]

is_none_time = timeit.timeit("is_none(None)", setup="from __main__ import is_none", number=1000)
is_equal_none_time = timeit.timeit("is_equal_none(None)", setup="from __main__ import is_equal_none", number=1000)

is_none_integers_time = timeit.timeit("is_none(x)", setup="from __main__ import is_none, integers; x=integers", number=1000)
is_equal_none_integers_time = timeit.timeit("is_equal_none(x)", setup="from __main__ import is_equal_none, integers; x=integers", number=1000)

is_none_datetimes_time = timeit.timeit("is_none(x)", setup="from __main__ import is_none, datetimes; x=datetimes", number=1000)
is_equal_none_datetimes_time = timeit.timeit("is_equal_none(x)", setup="from __main__ import is_equal_none, datetimes; x=datetimes", number=1000)

print("Performance test results:")
print("---------------------------")
print(f"Execution time of is_none(): {is_none_time} seconds")
print(f"Execution time of is_equal_none(): {is_equal_none_time} seconds")

print("\nInteger comparison:")
print("---------------------------")
print(f"Execution time of is_none() for integers: {is_none_integers_time} seconds")
print(f"Execution time of is_equal_none() for integers: {is_equal_none_integers_time} seconds")

print("\nDatetime comparison:")
print("---------------------------")
print(f"Execution time of is_none() for datetimes: {is_none_datetimes_time} seconds")
print(f"Execution time of is_equal_none() for datetimes: {is_equal_none_datetimes_time} seconds")

bytecode = dis.Bytecode(is_none)
print("\nInstructions for is_none():")
for instruction in bytecode:
    print(instruction)

bytecode = dis.Bytecode(is_equal_none)
print("\nInstructions for is_equal_none():")
for instruction in bytecode:
    print(instruction)
