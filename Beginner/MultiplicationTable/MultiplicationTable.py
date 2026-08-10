print("Welcome to the 'Multiplication Table'!")
number=input("What's your number? ")

#Checking whether the input is a digit or not.
while not number.isdigit():
    number=input("Please enter a digit! ")
number=int(number)

for i in range (13):
    print(number,"*",i,"=",number*i)