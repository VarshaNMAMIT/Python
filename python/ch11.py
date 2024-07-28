# class two_d:
#     def __init__(self,i,j):
#         self.i=i
#         self.j=j
#     def show(self):
#         print(f" vectors are {self.i}i and {self.j}j")
# class three_d(two_d):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k=k
#     def show(self):
#         print(f" vectors are {self.i}i and {self.j}j and {self.k}k")
# v=two_d(4,5)
# f=three_d(4,9,8)
# v.show()
# f.show()
# ---------------------------------------------------------
# class animal:
#     def __init__(self):
#         print("I am belonging to animal family")
# class pets(animal):
#     def __init__(self):
#         super().__init__()
#         print("I am belonging to pet family")
# class dog(pets):
#     def bark(self):
        
#         print("dog is barking")
# d=dog()
# d.bark()
# -----------------------------------------------------------
# 6
class m:
    def __str__(self,i,j,k):
        print(f"vector is as follows{i}i+{j}j+{k}k")
s=m()
print(f"enter the dimentions of a 3d vector:")
i=int(input("enter coefficient along i:"))
j=int(input("enter coefficient along j:"))
k=int(input("enter coefficient along k:"))
s.__str__(i,j,k)
