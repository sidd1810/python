for row in range(0,7):
    for col in range(0,7):
        if (col==0 or col==6) or (row==0 and col==1) or (row==1 and col==1) or (row==2 and col==2) or (row==3 and col==3) or (row==2 and col==4) or(row==1 and col==5) or (row==0 and col==5):
            print("*",end="")
        else:
            print(end=" ")
    print()