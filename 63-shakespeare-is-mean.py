#http://www.pangloss.com/seidel/shake_rule.html

import random

first_words = ["bootless", "churlish", "goatish"]
second_words = ["boil-brained", "crook-pated", "hedge-born"]
third_words = ["canker-blossom", "flap-dragon", "maggot-pie"]

first = random.choice(first_words)
second = random.choice(second_words)
third = random.choice(third_words)

insult = f"Thou {first} {second} {third}!!!"
print(insult)