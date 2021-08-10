"""Health Management System
       3 Clients - Harry, Rohan & Hammmad
       """

def getdate():
    import datetime
    return datetime.datetime.now()


#Total 6 files
"""Write a function that when 
     executed takes as input client 
      [] name cable crossover

      One more function toretrieve exercise
      or food for any client
     """

def take(k):
    if k == 1:
        c = int(input("Enter your choice for the parameters of health : \n"))
        if c == 1:
            print("Enter the value for exercise: \n")
            value = input("Type Here \n")
            with open("vikash.txt", "a") as opn:
                opn.write(str([str(getdate())])+ ":" + value + "\n")
            print("Successfully Written \n")
        elif c == 2: 
            print("Enter the value for Diet:\n")
            value = input("Type Here \n")
            with open("vikash.txt", "a") as opn:
                opn.write(str([str(getdate())])+ ":" + value + "\n")
            print("Successfully Written \n")
    elif  k == 2: 
        c = int(input("Enter your choice for the parameters of health: \n"))
        if c == 1:
            print("Enter the value for excercise: \n")
            value = input("Type Here \n")
            with open("rohan.txt", "a") as opn:
                opn.write(str([str(getdate())])+ ":" + value + "\n")
            print("Successfully Written \n")
        elif c == 2: 
            print("Enter the value for Diet:\n")
            value = input("Type Here \n")
            with open("rohan.txt", "a") as opn:
                opn.write(str([str(getdate())])+ ":" + value + "\n")
            print("Successfully Written \n")
    else:
        print("Enter the correct value: \n")


               


def retrieve(k):
    if k == 1: 
        c = int(input("Enter your choice for the parameters of health: \n"))
        if c == 1:
            print("Get the values for excercise: \n")
            with open("vikash.txt") as oppn:
                for i in oppn: 
                    print(i, end = "")
        elif c == 2:
            print("the values for Diet: \n")
            with open("vikash.txt") as oppn:
                for j in oppn:
                    print(j, end = "")

    elif k == 2: 
        c = int(input("Enter your choice for the parameters of health: \n"))
        if c == 1:
            print("Get the values for excercise: \n")
            with open("rohan.txt") as oppn:
                for i in oppn: 
                    print(i, end = "")
        elif c == 2:
            print("the values for Diet: \n")
            with open("rohan.txt") as oppn:
                for j in oppn:
                    print(j, end = "")

    else:
        print("Enter the correct value: \n")


    


clients = {"1": "Vikash", "2":"Rohan"}
healthParams = {"1":"Excercise", "2":"Diet"}
print("Clients: \n", clients)
print("healthParams: \n", healthParams)

a = int(input("Enter 1 for writing to the file and 2 for retrieving the data from the file: \n"))
print("Your Choice: \n", a)
if a == 1:
    b = int(input("Enter the choice for clients: \n"))
    take(b)
else:
    b = int(input("Enter the choice for clients"))
    retrieve(b)


