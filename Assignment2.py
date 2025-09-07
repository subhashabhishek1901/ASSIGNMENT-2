'''
#TASK-1
n=int(input("Enter the number"))
if n%2==0:
    print("the no. ",n,"is even number")
else:
    print("the no. ",n,"is odd number")
print("thankyou")'''



#TASK-2
n=list(range(1,51))
sum=0
for i in n:
    sum=sum+i
    print("the sum of first 50 natural no. is:",sum)