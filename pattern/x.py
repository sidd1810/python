for row in range(0,7):
    for col in range(0,7):
        if (col==row) or (row==0 and col==6) or (row==1 and col==5) or (row==2 and col==4) or (row==4 and col==2) or (row==5 and col==1) or(row==6 and col==0):
            print("*",end="")
        else:
            print(end=" ")
    print()