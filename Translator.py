from googletrans import Translator
t=Translator()
a=input("Enter any word:")
b=input("Enter target lang:")
res=t.translate(a,des=b)
print(res.text)
