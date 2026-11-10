a = [12, 4, 9, 1, 6, 3]
b = a.copy()
a1 = []
a2 = []

f1 = 0
l2 = len(a)-1
f2 = (f1+l2)//2+1
l1 = f2
while (len(a)>0) :
   min1 = a[f1]
   min2 = a[f2]
   for i in range(f1,l1):
      if a[i]<min1 :
         min1 = a[i]
   a.remove(min1)
   a1.append(min1)
   for j in range(f2,l2):
      if b[j]<min2 :
         min2 = b[j]
   b.remove(min2)
   a2.append(min2)

print(a1.append(a2))

