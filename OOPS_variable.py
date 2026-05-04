class abc:
    def set_dim(self,a,b):
        self.total=a+b
    def display(self):
        print("Addition is: ",self.total)
a=abc()
b=abc()
a.set_dim(20,30)
b.set_dim(30,40)
a.display()
b.display()
