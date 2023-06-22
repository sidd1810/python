
for  row in range(0,7):
    for col in range(0,5):
        if (col==0 or col==4) or (row==0 or row==3 or row==6) and (col>0 and col<4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

    #pala com nu badhu opatai devanu pachi or no use karvo and cheela ma row ma bi or and cheela jya *
    #* print na karvano hiy tya end mukvanoi 
    #cheele print " " a jagyaa khali re jagya aena mate chee 
    