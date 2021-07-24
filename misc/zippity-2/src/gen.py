import string
import random

choices = string.ascii_letters + string.digits + '!#$%&+-?@'

for i in range(6842):
    with open(f'boogaloo-{i}.txt', 'w') as f:
        f.write('NEWBIE{' + ''.join(random.choice(choices) for _ in range(random.randint(16, 32))) + '}')
