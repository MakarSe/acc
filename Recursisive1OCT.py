n1 = int(input("Number of terms: "))

def function1(n1):

    n2 = 0
    n3 = 1

    counter = 0



    if n1 <= 0:
        print("Enter a number above 0: ")
    else:
        while counter < n1:
            print(n2)
            
            n4 = n2 + n3
            
            n2 = n3
            n3 = n4
            counter += 1

function1(n1)
