#1 Strange Zoo
# pos1 = input()
# pos2 = input()
# pos3 = input()
# animal = [pos1, pos2, pos3]
# animal.reverse()
# print(animal)


#2 Courses
# num = int(input())
# courses =[]
# for i in range(0, num):
#     course = input()
#     courses.append(course)
#
# print(courses)


#3 List Statistics
# num = int(input())
# positive = []
# negative = []
#
# for _ in range(0, num):
#     integer = int(input())
#     if integer >= 0:
#         positive.append(integer)
#     else:
#         negative.append(integer)
#
# print(positive)
# print(negative)
# print(f'Count of positives: {len(positive)}')
# print(f'Sum of negatives: {sum(negative)}')


#4 Search
# num = int(input())
# word = input()
# strings = []
# for _ in range(0, num):
#     string = input()
#     strings.append(string)
#
# print(strings)
#
# for i in range(len(strings) -1, -1, -1):
#     element = strings[i]
#     if word not in element:
#         strings.remove(element)
#
# print(strings)


#5 Numbers Filter
# num = int(input())
# numbers = []
# filtered =[]
# for _ in range(0, num):
#     integer = int(input())
#     numbers.append(integer)
#
# command = input()
# if command == 'even':
#     for number in numbers:
#         if number % 2 == 0:
#             filtered.append(number)
# elif command == 'odd':
#     for number in numbers:
#         if number % 2 != 0:
#             filtered.append(number)
# elif command == 'negative':
#     for number in numbers:
#         if number < 0:
#             filtered.append(number)
# elif command == 'positive':
#     for number in numbers:
#         if number >= 0:
#             filtered.append(number)
#
# print(filtered)


#1 Invert values
# string_num = input().split()
# inverse = []
# for num in string_num:
#     number = -int(num)
#     inverse.append(number)
#
# print(inverse)


#2 Multiples list
# factor = int(input())
# count = int(input())
# list_num = []
# for multiplier in range(1, count + 1):
#     list_num.append(multiplier * factor)
#
# print(list_num)


#3 Football cards
# # team_a = ['A-' + str(s) for s in range(1, 12)]
# # team_b = ['B-' + str(s) for s in range(1, 12)]
# team_a = ['A-1', 'A-2', 'A-3', 'A-4', 'A-5', 'A-6', 'A-7', 'A-8', 'A-9', 'A-10', 'A-11']
# team_b = ['B-1', 'B-2', 'B-3', 'B-4', 'B-5', 'B-6', 'B-7', 'B-8', 'B-9', 'B-10', 'B-11']
# players = input().split()
# game_terminated = False
# for player in players:
#     if player in team_a:
#         team_a.remove(player)
#     elif player in team_b:
#         team_b.remove(player)
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_terminated = True
#         break
# print(f'Team A - {len(team_a)}; Team B - {len(team_b)}')
# if game_terminated:
#     print('Game was terminated')


#4 Number Beggars
numbers = input().split(', ')
beggars_count = int(input())
list_sums = []
starting_index = 0
numbers_digits = []
for number in numbers:
    numbers_digits.append(number)
while starting_index < beggars_count:
    sum_for_current_beggar = 0
    












