w =["Saturday","Sunday","Monday","Tuesday","Wednesday","Thursday","Friday"]
y = int(input("Enter year: "))

mm = int(input("Enter month: "))
if mm==1:
    mm=13
    y=y-1


elif mm==2:
    mm=14
    y=y-1



dd = int(input("Enter the day of month: "))

c = y//100
k = y%100

h = (dd +(13*(mm+1))//5 + k + k//4 +c//4 -2*c) % 7

print("Day of week is: ", w[h] )