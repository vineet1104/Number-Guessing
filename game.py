import random

number = random.randint(1, 20)

player_name = input("Hello, What is your name?")
number_of_guesses = 0
print('Okay!,' + player_name + ' I am guessing the number between 1 and 20')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break

if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))