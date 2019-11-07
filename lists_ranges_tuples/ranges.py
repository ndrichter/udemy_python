decimals = range(0, 100)
my_range = decimals[3:40:3]

# true
print(my_range == range(3, 40, 3))

#  true
print(range(0, 5, 2) == range(0, 6, 2))

# [0, 2, 4]
print(list(range(0, 5, 2)))
print(list(range(0, 6, 2)))


r = range(0, 100)
print(r)

# print backwards from 99 by 2
for i in r[::-2]:
    print(i)

print('=' * 50)

# also prints backwards from 99 by 2
for i in range(99, 0 , -2):
    print(i)

# true
print(range(0, 100)[::-2] == range(99, 0, -2))

# nothing prints
for i in range(0, 100, -2):
    print(i)

# Python is a very powerful language
backString = "egaugnal lufrewop yrev a si nohtyP"
print(backString[::-1])

# countdown from 9
r = range(0, 10)
for i in r[::-1]:
    print(i)

