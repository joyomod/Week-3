# TASK 1
# question 1
import math
import requests
from pprint import pprint as pp
from num2words import num2words

question = input('Is it sunny outside? ')
if question == 'y':
    print('Take your sunglasses')
elif question == 'n':
    print('You don\'t need sunglasses')
else:
    print("can you answer with yes or no")

# question 2

# Problems with solutions
# 1 - Syntax error (the venue_cost wasn't properly named; amended it to follow snakecase naming convention in python)
# 2 - Name error (the hours variable wasn't defined; changed the 'hour' variable to 'hours')
# 3 - Syntax error (the second print function required a closing bracket; added a closing bracket)
# 4 - Type error (the operator '<' cannot compare the string 'my_money' and a float 'venue_cost';
#     converted my_money to float

# addition - changed the operator '<' to '<=' to allow for equal to

my_money = input('How much money do you have? ')
hours = 3
venue_cost = (200 * hours) + 1.1

if int(my_money) <= venue_cost:
    print('You cannot afford the venue')
else:
    print('You can afford the venue')


# question 3

def tens_ones(arg):
    divisible_by_ten = math.floor(arg / 10)
    remainder = arg % 10

    if arg > 25 or arg < 1:
        print('You must enter a number between 1 and 25')
    elif (1 <= arg <= 25) and (divisible_by_ten <= 1) and (remainder <= 1):
        print(f"{(num2words(divisible_by_ten)).capitalize()} Ten, {(num2words(remainder)).capitalize()} One")
    elif (1 <= arg <= 25) and (divisible_by_ten > 1) and (remainder <= 1):
        print(f"{(num2words(divisible_by_ten)).capitalize()} Tens, {(num2words(remainder)).capitalize()} One")
    elif (1 <= arg <= 25) and (divisible_by_ten <= 1) and (remainder > 1):
        print(f"{(num2words(divisible_by_ten)).capitalize()} Ten, {(num2words(remainder)).capitalize()} Ones")
    else:
        print(f"{(num2words(divisible_by_ten)).capitalize()} Tens, {(num2words(remainder)).capitalize()} Ones")


while True:
    st_put = int(input('Enter a number between 1 and 25: '))
    if 1 <= st_put <= 25:
        tens_ones(st_put)
        break
    else:
        print('You must enter a number between 1 and 25.')

# TASK 2
# question 1
# Problem/Solution - The index position to get the first name is given as 1 when it ought to be 0

students = ['Chloe', 'Anna', 'Lauren', 'Shreya', 'Siobhan']
print(sorted(students)[0])

# question 2
shop = {
    "sofa": 2340,
    "console": 300,
    "bookcase": 220,
    "stool": 250,
    "desk": 280
}


def boot_sale(arg):
    for item in shop:
        price = shop[item]
        if item == arg:
            print(price)


boot_sale('stool')

# question 3

times_rolled = 100
information = int(input('You have two dice. What number they are trying to get? '))


def dice_roll(arg):
    score_per_roll = 0
    print('dice roll')


dice_roll(information)

# TASK 3

lyrics = """Well, my friends, the time has come
To raise the roof and have some fun
Throw away the work to be done
Let the music play on (play on, play on, play on...)
Everybody sing, everybody dance
Lose yourself in wild romance
We're going to Party, Karamu, Fiesta, forever
Come on and sing along!

All night long (all night), All night (all night)
All night long (all night), All night (all night)
All night long (all night), All night (all night)
All night long! (all night), Ooh, yeah (all night)

People dancing all in the street
See the rhythm all in their feet
Life is good, wild and sweet
Let the music play on...(Play on, play on, play on...)
Feel it in your heart and feel it in your soul
Let the music take control
We're going to Party, Liming, Fiesta, forever
Come on and sing along
We're going to Party, Liming, Fiesta, forever
Come on and sing my song!"""

with open('song.txt', 'w') as file:
    file.write(lyrics)

with open('song.txt', 'r') as file:
    new_lyrics = file.readlines()

for line in new_lyrics:
    if 'sing' in line:
        print(line.strip())


# Task 4

# pokemon_number = input("What is the Pokemon's ID? ")
# url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_number}/'
#
# response = requests.get(url)
# data = response.json()
# pp(data)

pokemon_ids = [1, 2, 3, 4, 5, 6]
with open('pokemon.txt', 'w') as txt_file:
    for pokeman in pokemon_ids:
        response = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokeman}')
        data = response.json()
        name = data['name']
        height = data['height']
        weight = data['weight']
    txt_file.write(f"{name}, Height: {height}, Weight: {weight}\n")
