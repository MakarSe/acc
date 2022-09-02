import csv
#f = open("data.csv", "w", newline = "")

# str1 = ["Title,First,Name,Surname,Address,City,Postcode,Telephone"]
# str2 = ["Mr,Tom,Smith,42,Mill,Street,London,WE13GW,10344044"]
# str3 = ["Mrs,Sandra,Jones,10,Low,Lane,Hull,HU237HJ,22344033"]
# str4 = ["Mr,John,Jacob,8,Sherlock,Court,Cambridge,CB30JB,55007788"]
# 
# db = csv.writer(f)
# db.writerow(str1)
# db.writerow(str2)
# db.writerow(str3)
# db.writerow(str4)
# 
# f.close()

f2 = open("yes.csv" , "r")
data = list(csv.reader(f2))

f2.close()
for i in data:
    print (i[7])



