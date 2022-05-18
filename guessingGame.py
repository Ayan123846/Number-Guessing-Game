import random
print("By Mohd. Ayan")
print("To Ms. Rahat Shaikh")
print("Number Guessing Game")
number = random.randint(1, 10)
chanceCount = 0
print("Guess a number (between 1 and 10):")
print("Rule : You have 5 chances.")

while chanceCount < 5:
    introString = int(input("Your Guess Here :- "))

    if (introString == number):
        print("Congratulations!!! Your Guess is correct!!")
        break

    elif (introString < number):
        print("OHH NO! Your guess is too low! Your guess should be higher than", introString)

    else :
        print("OHH NO! Your guess is too high! Your guess should be lower than", introString)

    chanceCount += 1

if not chanceCount < 5:
    print("OHH NO!!! Your guess is wrong!!")
    print("The number is", number)