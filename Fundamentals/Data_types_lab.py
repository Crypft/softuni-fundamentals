# #1 Concat names
# first_name = input()
# last_name = input()
# delimiter = input()
#
# print(f'{first_name}{delimiter}{last_name}')


# #2 Convert meters to kilometers
# meters = int(input())
# km = meters / 1000
# print(f'{km:.2f}')



# #3 Pounds to dollars
# pound = int(input())
# dollars = pound * 1.31
# print(f'{dollars:.3f}')


# #4 Centuries to minutes
# centuries = int(input())
# years = centuries * 100
# days = int(years * 365.2422)
# hours = days * 24
# minutes = hours * 60
# print(f'{centuries} centuries = {years} years = {days} days = {hours} hours = {minutes} minutes')



# #5 Special numbers
# n = int(input())
#
# for num in range(1, n+1):
#     sum_digits = 0
#     digits = num
#
#     while digits > 0:
#         sum_digits += digits % 10
#         digits = int(digits/10)
#
#     if (sum_digits == 5) or (sum_digits == 7) or (sum_digits == 11):
#         print(f'{num} -> True')
#     else:
#         print(f'{num} -> False')


#6 Next happy year
year = int(input())
happy_year = False

while not happy_year:
    year += 1
    set_year = set()
    for i in range(len(str(year))):
        set_year.add(str(year)[i])

    happy_year = len(set_year) == len(str(year))

print(year)



















