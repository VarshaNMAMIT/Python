class Train:
    def __init__(self,name,sea,fare,tickets):
        self.name=name
        self.sea=sea
        self.fare=fare
        self.tickets=tickets
    def book(self):
        print(f"you are booking: {self.name}")
    def status(self):
        print(f"total available seats:{self.sea}")
    def fares(self):
         print(f"you are paying: {(self.fare)*(self.tickets)}")
seats={
    "decan":400,
    "odyssey":500,
    "belmond":200,
    "maharaja":60
}
fare={
    "decan":1000,
    "odyssey":2000,
    "belmond":500,
    "maharaja":10000
}
name=input("enter the name of the train:")
s=seats[name]
tickets=int(input("enter total number of tickets:"))
t=Train(name,s,fare[name],tickets)
fare[name]=fare[name]-tickets
t.book()
t.status()
t.fares()

