def sq():
    s=int(input("Enter size"))
    print("Area: ",s*s)
def rect(l,b):
    print("AREA: ",l*b)
def cir():
    r=int(input("Enter radius:"))
    return 3.14 * r * r
def tri(b,h):
    return 0.5*h*b
while True:
    print("1.Square")
    print("2.Rectangle")
    print("3.Circle")
    print("4.Rectangle")
    print("5.Exit")
    ch=int(input("Enter Varnitha_40your choice:"))
    if ch==1:
        sq()
    elif ch==2:
        l=int(input("Enter len:"))
        b=int(input("Enter breadth:"))
        rect(l,b)
    elif ch==3:
        x=cir()
        print("Area",x)
    elif ch==4:
        b=int(input("Enter base:"))
        h=int(input("Enter height:"))
        y=tri(b,h)
        print("Area",y)
    else:
        break;
