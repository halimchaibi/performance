import dis
import timeit
import datetime
from faker import Faker

fake = Faker()

def is_none(x):
    return x is not None

def is_equal_none(x):
    return x != None



integer_value = fake.random_int() 
date_time_value = fake.date_time()

is_none_time = timeit.timeit("is_none(None)", globals=globals(), number=100)
is_equal_none_time = timeit.timeit("is_equal_none(None)", globals=globals(), number=100)

is_none_integers_time = timeit.timeit("is_none(x)", globals=globals(), setup="x=integer_value", number=100)
is_equal_none_integers_time = timeit.timeit("is_equal_none(x)", globals=globals(), setup="x=integer_value", number=100)

is_none_datetimes_time = timeit.timeit("is_none(x)", globals=globals(), setup="x=date_time_value", number=100)
is_equal_none_datetimes_time = timeit.timeit("is_equal_none(x)", globals=globals(), setup="x=date_time_value", number=100)




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

x = 1
if x.__eq__(None):
    print("1 is equal to None")




