row=7
col=5
for row in range(0,7):
    for col in range(0,7):
        if (col==1 ) or (row==0 or row==6) and (col>0 and col<7):
            print("*",end="")
        else:
            print(" ",end=" ")
    print("")




            
