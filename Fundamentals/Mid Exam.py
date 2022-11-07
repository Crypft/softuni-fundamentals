# 1 Cooking Masterclass
# from math import ceil, floor
# budget = float(input())
# students = int(input())
# price_package_flour = float(input())
# price_single_egg = float(input())
# price_apron = float(input())
#
# free_packages = 0
# if students > 4:
#     free_packages = students / 5
# total_price = students * price_single_egg * 10 + price_apron * (students + (ceil(0.2 * students))) \
#     + price_package_flour * (students - floor(free_packages))
#
# neededMoney = abs(budget - total_price)
#
# if total_price <= budget:
#     print(f"Items purchased for {total_price:.2f}$.")
# else:
#     print(f"{neededMoney:.2f}$ more needed.")


# 2 Numbers
numbers_sequence = input().split(' ')
list_of_numbers = numbers_sequence.copy()

while True:
    command = input()

    if command == 'Finish':
        print(' '.join(list_of_numbers))
        break

    command_list = list(command.split())
    command_name = command_list[0]
    value = command_list[1]
    replacement = 0
    if len(command_list) > 2:
        replacement = command_list[2]

    if command_name == 'Add':
        list_of_numbers.append(value)
    elif command_name == 'Remove':
        if value in list_of_numbers:
            list_of_numbers.remove(value)
        else:
            continue
    elif command_name == 'Replace':
        if value in list_of_numbers:
            index_value = list_of_numbers.index(value)
            list_of_numbers.remove(value)
            list_of_numbers.insert(index_value, replacement)
        else:
            continue
    elif command_name == 'Collapse':
        flag = True
        while flag:
            current_number = list_of_numbers[0]
            if int(current_number) < int(value):
                list_of_numbers.remove(current_number)

            if int(current_number) > int(value):








            # current_number = list_of_numbers[0]
            # if int(i) < int(current_number):
            #     current_number = i
            # if int(current_number) < int(value):
            #     list_of_numbers.remove(current_number)
            # else:
            #     continue


# 3 Deck of cards
# cards_list = input().split(', ')
# n = int(input())
#
# for i in range(0, n):
#
#     command = input()
#     command_list = list(command.split(', '))
#     command_name = command_list[0]
#     card = command_list[1]
#     if len(card) < 5:
#         if len(command_list) > 2:
#             card = command_list[2]
#         index = int(command_list[1])
#
#     if command_name == 'Add':
#         if card in cards_list:
#             print('Card is already in the deck')
#             continue
#         else:
#             cards_list.append(card)
#             print('Card successfully added')
#     elif command_name == 'Remove':
#         if card not in cards_list:
#             print('Card not found')
#             continue
#         else:
#             cards_list.remove(card)
#             print('Card successfully removed')
#     elif command_name == 'Remove At':
#         if index > len(cards_list):
#             print('Index out of range')
#             continue
#         else:
#             del cards_list[index]
#             print('Card successfully removed')
#     elif command_name == 'Insert':
#         if index > len(cards_list) or index < 0:
#             print('Index out of range')
#             continue
#         if index <= len(cards_list) and card in cards_list:
#             print('Card is already added')
#         else:
#             cards_list.insert(index, card)
#             print('Card successfully added')
#
# print(', '.join(cards_list))