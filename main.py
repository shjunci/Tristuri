def lenkuParbaude(len1,len2,len3):
  rezultats=False
  if len1+len2+len3==180:
    rezultats=True
  return rezultats

len1=int(input("Ievadiet 1.leņki: "))
len2=int(input("Ievadiet 2.leņki: ")) 
len3=int(input("Ievadiet 3.leņki: "))
rez=lenkuParbaude(len1,len2,len3)
if rez:
  print("Trissturis eksiste")
else:
  print("Trissturis eksiste")  