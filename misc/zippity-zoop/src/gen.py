import string
import random

choices = string.ascii_letters + string.digits + '!#$%&+-?@'

for i in range(0, 2**14):
    with open(f'zoop-{i}.txt', 'w') as f:
        f.write(''.join(random.choice(string.ascii_uppercase) for _ in range(6)) + '{' + ''.join(random.choice(choices) for _ in range(random.randint(16, 32))) + '}')
