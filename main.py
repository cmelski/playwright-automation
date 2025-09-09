a, b, c = 5, 6, 7

print("{} {}".format("Value is", b))
print(f'Value is {b}')

print(type(b))

dict1 = dict()

dict1['firstname'] = 'Chris'

print(dict1.items())

sum_num = 0
for i in range(1, 6):
    sum_num += i
print(sum_num)
sum_num = 0
for i in range(1, 10, 2):
    sum_num += i
print(sum_num)

i = 10

while i > 1:
    if i == 9:
        i -= 1
        continue
    if i == 3:
        break


    print(i)
    i -= 1

with open('text.txt', 'r') as file:
    content = file.readlines()

with open('text.txt', 'w') as file:
    content = content[::-1]
    for item in content:
        file.write(item)

print(content)



