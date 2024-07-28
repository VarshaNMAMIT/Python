# d={"kaise":"how","tum":"you","mujhe":"me"}
# v=input("enter word to lookup:")
# print(d[v])
# a=set()
# for i in range (0,8):
#     e=int(input(f"enter number {i+1}:"))
#     a.add(e)
# print(f"unique numbers are{a}")
# a={18,'18'}
# print(a)
# s=set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(len(s))
# print(s)
# x={}
# print(type(x))
d={}
for i in range(0,2):
    k=input("enter friend name:")
    v=input("enter  language:")
    d.update({k:v})
print(d)
