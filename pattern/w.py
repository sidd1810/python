for row in range(0,7):
    for col in range(0,7):
        if (col==0 or col==6) or (col==row and (row!=0 and row!=1 and row!=2)) or (row==4 and col==2) or(row==5 and col==1):
            print("*",end="")
        else:
            print(end=" ")
    print()
