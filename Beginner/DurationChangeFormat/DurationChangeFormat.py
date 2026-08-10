#Welcome the user
print("Welcome to 'Duration Change Format'\nWhere you input your duration in seconds and get it back in (Hours, Minutes and Seconds).")
#Input the user's duration
sec=float(input("Enter the duration in seconds: "))
#Change the duration format
hours=int(sec//3600)
minutes=int((sec%3600)//60)
seconds=round(sec%60,2)
#Show result
print("The duration is: ",hours," hours, ",minutes," minutes, ",seconds," seconds.")