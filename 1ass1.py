n=int(input("Enter a number:"))
num1=0
while(n>0):
    dig=n%10
    num1=num1+dig
    n=n//10
print("The total sum of digits is:",num1)