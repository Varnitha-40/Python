for i in range(100,1000):
    c=0 #if we  apply before like 1st step it can't update it resets from 1st (0) 
    for j in range(2,i):
        if i%j==0:
            c=c+1
    if c==0:
        print(i,end=" ")
