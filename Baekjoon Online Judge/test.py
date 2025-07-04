import random

a = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(10)]
a.sort(reverse = True)
print(a)