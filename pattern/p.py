for row in range(0,5):
    for col in range(0,5):
        if (col==0 or col==4) or (row==0 or row==4 and (col>0 and col<4)):
            print("*",end="")
        else:
            print(end=" ")
    print()
                  