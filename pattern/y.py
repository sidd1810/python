for row in range(0,5):
    for col in range(0,5):
        if (col==2s and(row!=0 and row!=1 )) or (row==col and col<2) or (row==1 and col==3) or(row==0 and col==4):
            print("*",end="")
        else:
            print(end=" ")
    print()
