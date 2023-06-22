row=7
col=5
for row in range(0,7):
    for col in range(1,6):
        if (col==5) or (row==0 or row==3) and (col>1 and col<6):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()    