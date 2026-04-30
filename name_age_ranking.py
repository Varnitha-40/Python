names=["Ram","Raj","Rose","Jack","Pavi"]
age=[34,56,20,12,89]
res=list(zip(age,names))
res1=sorted(res)
pos=1
for i in res1:
    print("Rank {}: {} age is {} yrs old".format(pos,i[1],i[0]))
    pos=pos+1
