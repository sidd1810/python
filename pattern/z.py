for row in range(0,7):
    for col in range(0,7):
        if (row==0 or row==6) or (row==1 and col==5) or (row==2 and col==4) or (row==3 and col==3) or (row==4 and col==2) or (row==5 and col==1):
            print("*",end="")
        else:
            print(end=" ")
    print()