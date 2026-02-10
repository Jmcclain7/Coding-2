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