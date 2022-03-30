n1 = int(input("Enter a number: "))

def reSum(n):
    if n <= 1:
        return n
    return n + reSum(n - 1)
 
print(reSum(n1))
