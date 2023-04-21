# def say_hi(name):
#     print(f"Hello there, {name}")
#     
# say_hi("Abeeha")


def add_them(number1, number2):
    answer = number1 + number2
    return answer

num = input("What's the first number? ")
num2 = input("What's the second number? ")

num = int(num)
num2 = int(num2)

result = add_them(num, num2)
print(result)
