import random


print('haha')
print(123)
print('大樂透')
print('test1')
print('你好')
a = set(
)
b = []

nuber = random.randint(1,49)
# print(nuber)

while True:
    nuber = random.randint(1,49)
    a.add(nuber)
    if len(a) == 6:
        while True:
            number = random.randint(1,49)
            if number not in a:
                print(f"大樂透號碼為{a},特別號為{number}")
                break
        break

