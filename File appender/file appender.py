temp = open("Student.txt", "a")

name = input("Enter a students name (input stop to terminate):\n")

while name != "stop":

    username = input("Enter username: ")
    surname = input("Enter surname:\n")
    gender = input("Enter gender:\n")
    year = input("Enter year:\n")
    temp.write(username + "," + name + "," + surname + "," + gender + "," + year + "\n")
    name = input("Enter a students name (input xxx to terminate):")

temp.close()

myFile = open("Student.txt", "r")
list1 = []
list2 = []

for row in myFile:
    list1 = row.split(",")
    username1 = list1[0]
    fname = list1[1]
    sname = list1[2]
    gndr = list1[3]
    yr = int(list1[4])

    list2.append([username1, fname, sname, gndr, yr])

    list1.append(list2)

    list2 = []

for i in list1:
    print(i)
