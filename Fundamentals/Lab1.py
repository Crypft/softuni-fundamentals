#1 Number Definer

# number = float(input())
#
# if number == 0:
#     print('zero')
# elif 0 < number < 1:
#     print('small positive')
#
# if number > 100000:
#         print('large positive')
# elif 1 < number <= 1000000:
#         print('positive')
#
# if 0 > number > -1:
#     print('small negative')
#
# if number < -1000000:
#         print('large negative')
# elif -1 > number > -1000000:
#         print('negative')


#2 Largest of three numbers

# first = int(input())
# second = int(input())
# third = int(input())
#
# if first > second > third:
#     print(first)
# elif second > first > third:
#     print(second)
# else:
#     print(third)


#3 Word reverse

# word = str(input())
# reverse = ''
#
# for i in range(len(word) -1, -1, -1):
#     reverse += word[i]
#
# print(reverse)


#4 Even numbers

# n = int(input())
#
# for _ in range(n):
#     current = int(input())
#     if current % 2 != 0:
#         print(f'{current} is odd!')
#         break
#
# else:
#     print("All numbers are even.")


#5 Number Between 1 and 100
# current = 0
# while current < 1 or current > 100:
#     current = float(input())
#
# print(f'The number {current} is between 1 and 100')


#6 Shopping

# budget = int(input())
#
# while True:
#     cost = input()
#     if cost == 'End':
#         print('You bought everything needed.')
#         break
#
#     cost = int(cost)
#     budget -= cost
#
#     if budget < 0:
#         print('You went in overdraft!')
#         break



#7 Patterns
num = int(input())

for j in range(1, num + 1):
    for i in range(0, j):
        print('*', end='')
    print()

for j in range(num -1, 0, -1):
    for i in range(0, j):
        print('*', end='')
    print()