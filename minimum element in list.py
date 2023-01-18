list1=[]
n=int(input("enter the number of elements in list:"))
for i in range (1,n+1):
    e=int(input("enter numbers:"))
    list1.append(e)
print("minimum element is",min(list1))
