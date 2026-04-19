def change(ani):
    digit = (list(map(int,str(ani))))
    d2 = digit.copy()
    d2.reverse()
    if(digit == d2):
        print("yes")
    else:
        print("No")


change(50205)
