import random

die_1 = random.randrange(1, 7)
die_2 = random.randrange(1, 7)

print(f'''You rolled a {die_1}
You also rolled a {die_2}

That adds up to {die_1 + die_2}.''')
