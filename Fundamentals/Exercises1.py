#1 Jenny's Secret Message

# name = input()
#
# if name == 'Johnny':
#     print('Hello, my love!')
# else:
#     print(f'Hello, {name}!')


#2 Drink something

# age = int(input())
#
# if age <= 14:
#     print('drink toddy')
# elif 14 < age <= 18:
#     print('drink coke')
# elif 18 < age <= 21:
#     print('drink beer')
# elif age > 21:
#     print('drink whisky')


#3 Chat codes

# num = int(input())
#
# for _ in range(0, num):
#     code = int(input())
#     if code == 88:
#         print('Hello')
#     elif code == 86:
#         print('How are you?')
#     elif code != 86 and code < 88:
#         print('GREAT!')
#     elif code > 88:
#         print('Bye.')


#4 Maximum multiple

# divisor = int(input())
# boundary = int(input())
# N = boundary
# for _ in range(boundary, 0, -1):
#     if N % divisor == 0:
#         print(N)
#         break
#     else:
#         N -= 1


#5 Orders

# orders = int(input())
# total = 0
# for _ in range(0, orders):
#     price_per_capsule = float(input())
#     days = int(input())
#     capsules_per_day = int(input())
#
#     order_price = price_per_capsule * capsules_per_day * days
#
#     total += order_price
#     if order_price != 0:
#         print(f'The price for the coffee is: ${order_price:.2f}')
#
# print(f'Total: ${total:.2f}')


#6 String pureness

# num = int(input())
#
# for _ in range(0, num):
#     string = input()
#
#     x = "_" in string
#     y = "," in string
#     z = "." in string
#
#     if x or y or z:
#         print(f'{string} is not pure!')
#     else:
#         print(f'{string} is pure.')


#7 Double char

# while True:
#     string = input()
#     if string == 'End':
#         break
#
#     if string == 'SoftUni':
#         continue
#
#     for i in range(0, len(string)):
#       print(string[i] + string[i], end='')
#     print()


#8 How Much Coffee Do You Need?
# counter = 0
# while True:
#     event = input()
#     if event == 'END':
#         if counter > 5:
#             print('You need extra sleep')
#             break
#         else:
#             print(counter)
#             break
#
#     if event in ['coding', 'dog', 'cat', 'movie', 'CODING', 'DOG', 'CAT', 'MOVIE']:
#         if event.islower():
#             counter += 1
#         elif event.isupper():
#             counter += 2
#     else:
#         continue


#9 Sorting hat

# while True:
#     name = input()
#     if name == 'Welcome!':
#         print('Welcome to Hogwarts.')
#         break
#     if name == 'Voldemort':
#         print('You must not speak of that name!')
#         break
#
#     if len(name) < 5:
#         print(f'{name} goes to Gryffindor.')
#     elif len(name) == 5:
#         print(f'{name} goes to Slytherin.')
#     elif len(name) == 6:
#         print(f'{name} goes to Ravenclaw.')
#     elif len(name) > 6:
#         print(f'{name} goes to Hufflepuff.')


#12 * Easter bread

budget = float(input())
flour_kilo_price = flaot(input())







