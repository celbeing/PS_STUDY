import random
for i in range(1, 21):
    print(f'{i}: {'업' if random.randint(0, 1) else '다운'}')
