names=["Ram","Raj","Rose","Jack","Pavi"]
marks=[20,45,67,50,33]
pos=1
for i in range(5):
    if marks[i]>40:
        print("{}.{} has scored {}%".format(pos,names[i],marks[i]))
        pos=pos+1
