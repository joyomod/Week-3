# Week-3 Tasks

## TASK 1 (Conditional flow)

### Question 1
Create a program that tells you whether or not you need sunglasses when you leave the house.
The program should:
1. Ask you if it is sunny using input()
2. If the input is 'y', it should output 'Take your sunglasses’
3. If the input is 'n', it should output 'You don't need sunglasses’
 
### Question 2
I want to hire a venue for my birthday for 3 hours. The venue hire costs £200 per hour and a refundable 10% deposit. I've written a program to check that I can afford the cost, but something doesn't seem right. 
Have a look at my program and work out what I've done wrong:
` my_money = input('How much money do you have? ')
hour = 3
venue cost = (200*hours) + 1.1
if my_money < venue_cost:
  print('You can afford the venue')
else :
  print('You cannot afford the venue'`

### Question 3
You work as a primary school teacher and are teaching numbers by showing how they are composed of units of ten and one. Write a program for students to play with to understand this concept. You will be asking for them to enter numbers between 1 and 25 (they haven’t gone higher than that!), so you do not need to consider bigger numbers. The function needs to print to the screen and the message must be grammatically correct and in the format shown below.
For example:
●	If 15 was the input, the function output should be:
`One Ten, Five Ones`
●	If 21 was the input, the function output should be:
`Two Tens, One One`
●	If 20 was the input, the function output should be:
`Two Tens, Zero Ones`
●	If 8 was the input, the function output should be:
`Zero Tens, Eight Ones`


## TASK 2 (Lists and Dictionaries)

### Question 1
I have a list of students and I want to know after I sort the list, who is the first student in alphabetical order.
students = [“Chloe”, “Anna”, “Lauren”, “Shreya”, “Siobhan”]
print(sorted(students)[1])
However, when I run the program it shows me a different answer to what I was expecting? What is the mistake? How do I fix it?
### Question 2
You are trying to get rid of your old stuff in a bootsale and want to set up a program to quickly return the price when given an item.

●	Create a ‘shop’ dictionary with at least 4 items and respective prices. 
●	Write some code that will take in the name of an item and output the price

### Question 3
Write a program that simulates rolling two dice together 100 times. Record the results of each roll to know how many 2s, 3s, 4s, 5s, 6s, 7s, 8s, 9s, 10s, 11s and 12s were rolled. From this work out the probability of getting each number.
Tell the user they have two dice and ask them what number they are trying to get, then return the probability of them getting that number.
For example:
●	If 1 was the input, the output would be:
The chance of you getting 1 is 0%
●	If 7 was the input, the output would be:
The chance of you getting 7 is 12%
N.B.
Your probability may differ from this example.


 
## TASK 3 (Filter Files)
Here is a snippet of Lionel Richie’s song “All Night Long (All Night)”

`Well, my friends, the time has come
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
Come on and sing my song!`

Tasks:
1.	Write the lyrics to a new file called song.txt
2.	Read in the file and print out ONLY lines that have the word ‘sing’ in them. 

## TASK 4 (API)
In the API session you used the Pokémon API to retrieve a single Pokémon.
Now use a list to store 6 Pokémon IDs. In a for loop call the API to retrieve the data for each Pokémon. Save their names, height and weight into a file called 'pokemon.txt'
 
