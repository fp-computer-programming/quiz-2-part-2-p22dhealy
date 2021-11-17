#author: DMH 11/17/21

day = input("Please put in the day that it is(A-G)")

day = day.upper()

if day == 'A' or 'C' or 'E':
    print("You have class today")
elif day == 'B' or 'D' or 'F' or 'G':
    print("You do not have clas today")
else:
    print("Incorrect command")

    

