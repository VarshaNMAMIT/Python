# class programmer:
#     company="microsoft"
#     def __init__(self,name,age,gender):
#         self.name=name
#         self.age=age
#         self.gender=gender
#         print(self.name,self.age,self.gender)
#     print(company)
# varsha=programmer("varsha",20,"female")
# -----------------------------------------------------
# class calculator:
#     @staticmethod
#     def st():
#         print("greet the user")
#     def __init__(self,m):
#         self.m=m
#     def sq(slf):
#         print(slf.m*slf.m)
#      def cub(self):
#         print(self.m**3)
 #     def root(self):
  #         print(self.m**(0.5))
# c=calculator(9)
# c.st()
# c.sq()
# c.cub()
# c.root()
# --------------------------------------------------------
# class df:
#     a=1
# obj=df()
# b=df()
# obj.a=0
# print(obj.a)
# print(b.a)
# --------------------------------------------------------------
class train:
    def bookticket(self,book):
        print(f"you are booking train named {self.book}")
        
    def status(self,book,tick):
        if(book=="raj"):
            t=self.tick
            sr+=t
            total=200-sr
            print(f"number of seat available in {self.book} is {total}")
        elif(book=="aru"):
            t=self.tick
            sa+=t
            total=200-sa 
            print(f"number of seat available in {self.book} is {total}")
        elif(book=="mundri"):
            t=self.tick
            sm+=t
            total=200-sm
            print(f"number of seat available in {self.book} is {total}")
        elif(book=="thalavi"):
            t=self.tick
            st+=self.tick
            total=200-st
            print(f"number of seat available in {self.book} is {total}")
        elif(book=="local"):
            t=self.tick
            sl+=t
            total=200-sl
            print(f"number of seat available in {self.book} is {total}")
        else:
            print("enter valid one")

    def fare(self,ti,book):
        if(self.book=="local"):
            print(f"total fare is {ti*200}")
        else:
            print(f"total fare is {ti*400}")
p1=train()
tick=input("enter total number of tickets:")
book=input("enter the name of train:raj/aru/mundri/thalavi express/local")
p1.bookticket(book)
p1.status(book,tick)
p1.fare(tick,book)