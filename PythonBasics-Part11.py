# Let's learn about Object Oriented Programming

# Bad way of programming
class Car:
    pass

audiq7=Car()
audiq7

audiq7.millage=10
audiq7.year=2021
audiq7.make=345
audiq7.modle="latest"

audiq7.millage

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

nano1=Car() # will give you the error [TypeError: __init__() missing 4 required positional arguments: 'millage', 'year', 'make', and 'model']
nano1=Car(25,2020,3432,"twist")
audiq71=Car(10,2020,34332,"Q7")