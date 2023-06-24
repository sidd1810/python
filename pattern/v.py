for row in range(0,7):
    for col in range(0,7):
        if (col==row and(row!=4 and row!=5 and row!=6)) or (row==2 and col==4) or(row==1 and col==5) or (row==0 and col==6):
            print("*",end="")
        else:
            print(end=" ")
    print()