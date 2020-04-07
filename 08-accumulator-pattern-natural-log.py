def ln2():
    total = 1
    for denominator in range(2, 10000):
        if denominator % 2 == 0: #is it even?
            total = total - (1/denominator)
        else:
            total = total + (1/denominator)
    return total

print(ln2())