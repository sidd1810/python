row=7
col=5
for row in range(0,7):
    for col in range(0,5):
        if (col==0 ) or (row==0 or row==3 or row==6 ) and (col>0):
            print("*",end="")
        else:
            print(" ",end=" ")
    print()