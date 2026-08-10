print("Welcome to 'Where should the Rabbit go?' game!\nYou're gonna tell me where I need to place it.")

#Garden
row1=["🍃","🍃","🍃"]
row2=["🍃","🍃","🍃"]
row3=["🍃","🍃","🍃"]
print ("""
Here's the garden:
       
       ["🍃","🍃","🍃"]
       ["🍃","🍃","🍃"]
       ["🍃","🍃","🍃"]

       """)
#User order
answer=input("Okay, so where should the rabbit 🐰 go?\nPlease choose a row than a column (e.g. 31)")
row=int(answer[0])
column=int(answer[1])-1

if row>33:
    print("This is out of our terriotory!")
else:
    if row==1:
       row1.remove(row1[column])
       row1.insert(column,"🐰")
    elif row==2:
        row2.remove(row2[column])
        row2.insert(column,"🐰")
    else:
        row3.remove(row3[column])
        row3.insert(column,"🐰")

print(f"""
Moved successfully!
        {row1}
        {row2}
        {row3}
""")