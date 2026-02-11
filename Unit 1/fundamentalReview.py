# James McClain

# Put in a price and depending on the item price we will get 
# 15% or 25% off

#input, print, discount based pm itemPrice, function, program, 
#if/else
#50-75 = 15%
# 75>= 25%


def discount():
    itemPrice = int(input("please enter the item price. "))
    if itemPrice >= 50 and itemPrice <=75:
        discount = .15
        sum = itemPrice * discount
        total = itemPrice - sum
        Print("this is your final total "+ str(total))
    elif itemPrice >75:
        discount = .25
        sum = itemPrice * discount
        total = itemPrice - sum
        print("this is your final total "+ str(total))
    else:
        print("sorry, you do not get a discount.")

discount()

# check age, GPA, 





def qualifications(gpa, age):
    if gpa >= 90 and age >= 17:
        print('Congrats! You meet the req. for the job fair')
    else:
        print("Sorry, you dont meet req.") 

# qualificationsCheck(78, 17)



myGrades ={76, 87, 79, 84, 100, 81, 99, 72, 100, 98, 91}

def gpa():
    for grade in myGrades:
        if grade < 85:
            myGrades. remove(grade)
        print(myGrades)

    # function to remove() number from list
    # we will need a loop
    # if/else goal is to remove numbers > 85
    # boolean for the number