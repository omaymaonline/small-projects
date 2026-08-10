print("Welcome to your 'Mini Task Manager'!")

tasks=input("What are your tasks for today?\n(Please seperate between them using commas) ").split(", ")

while not tasks:
    tasks=input("What are your tasks for today?\n(Please seperate between them using commas) ").split(", ")

done_tasks=[]

#temp stands for temprory
for i in tasks:
    temp=input(f"Have you finished '{i}' already? (y/n)").lower()
    if temp=='y' or temp=='yes':
        print("Great!\n-------------------------\n")
        tasks.remove(i)
        done_tasks.append(i)
    elif temp=='n' or temp=='no':
        print("Try not to put it off!\n-------------------------\n")
    else:
        print("Invalid answer, I will take it as a no.\nTry not to put it off!\n-------------------------\n")

see_progression=input("Do you want to see your progression for today? (y/n)").lower()
if see_progression=='y' or see_progression=='yes':
    print(f"""
            ------Done Tasks------
          {done_tasks}

            ------ Ongoing Tasks ------
           {tasks}
    """)
elif see_progression=='n' or see_progression=='no':
    print("Okay!\nSee you!")
else:
    print("Invalid answer, I will take it as a 'yes'")
    print(f"""
            ------Done Tasks------
          {done_tasks}

            ------ Ongoing Tasks ------
           {tasks}
    """)