import random
print("Welcome to 'Who pays?'")
#Friends' list
friends=input("Enter your friends' names one by one, and I will pick one randomly to pay (please seperate them with commas)\n").split(", ")

#Random choice
friend=random.choice(friends)

print(f"'{friend}' is gonna pay for you tonight!")