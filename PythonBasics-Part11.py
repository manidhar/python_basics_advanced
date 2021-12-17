# Let's learn about Object Oriented Programming

# Bad programming practise
class Car:
    pass

audiq7=Car()
audiq7.millage=10
audiq7.year=2021
audiq7.make=345
audiq7.modle="latest"
print("Audi Q7 Milage: ",audiq7.millage," Audi Q7 Model :",audiq7.modle)


nano=Car()
nano.millage=20
nano.year=2021
nano.make=3453
nano.modle="twist"
nano.engine=34332423423
print(nano.millage,audiq7.millage)

# Good Programming practise
class Car:
    # Here self is not the key word. we can use any other name. for convinence we are using self
    # It is the pointer to itself
    def __init__(self,millage,year,make,model):
        self.millage=millage
        self.year=year
        self.make=make
        self.model=model
 # lets try to understand what self means here
 # self is the pointer to the object itself

nano1=Car() # will give you the error [TypeError: __init__() missing 4 required positional arguments: 'millage', 'year', 'make', and 'model']
nano1=Car(25,2020,3432,"twist")
audiq71=Car(10,2020,34332,"Q7")

print(nano1.millage,audiq71.millage)

class Car:
    # Here self is not the key word. we can use any other name. for convinence we are using self
    # Here a is behaving as self
    def __init__(a,mlg,yr,mk,mo):
        a.millage=mlg
        a.year=yr
        a.make=mk
        a.model=mo

nano2=Car(25,2020,3432,"twist")
# nano2.millage is a class variable
print(nano2.millage)

class Car:
    # Here self is not the key word. we can use any other name. for convinence we are using self
    # It is the pointer to itself
    def __init__(a,millage,year,make,model):
        a.millage=millage
        a.year=year
        a.make=make
        a.model=model

    def age(b,current_year):
        return current_year-b.year

    def milage(self):
        return self.millage

audiq72=Car(10,2019,34332,"Q7")
print(audiq72.age(2021))
print(audiq72.milage())
print(audiq72)

class Car:
    # Here self is not the key word. we can use any other name. for convinence we are using self
    # It is the pointer to itself
    def __init__(a,millage,year,make,model):
        a.millage=millage
        a.year=year
        a.make=make
        a.model=model

    def age(b,current_year):
        return current_year-b.year

    def milage(self):
        return self.millage

    def __str__(self):
        return "Car: "+self.model+" "+str(self.year)

audiq72=Car(10,2021,34332,"Q7")
print(audiq72)

class Student:

    def __init__(self,name,age,rollno):
        self.name=name
        self.age=age
        self.rollno=rollno

    def __str__(self):
        return "Student: "+self.name+" "+str(self.age)+" "+str(self.rollno)

    def str_rollno(self):
        if type(self.rollno)==int:
            print("Roll No: ",self.rollno)


    def name_parsing(self):
        if type(self.name)==list:
            for i in self.name:
                print("Name of student is : ",i)
        else:
            print("name is not a list type")


student1=Student("Raj",20,123)
print(student1.rollno)
print(student1.str_rollno())

moreStudents=Student(["Raj","Thasya","Samvedhya"],20,123)
print(moreStudents.name_parsing())

# Task
# Create a class called Data with the following attributes: file_name,file_type,date,size
# create function file_open() create file if not exists and write the data in it
# create function file_read() read the data from the file
# create function file_append() the date into file
# Implement expection handling and logger