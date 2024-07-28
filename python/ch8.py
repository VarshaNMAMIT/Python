# a=input("Enter a:")
# b=input("Enter b:")
# c=input("Enter c:")
# def great(a,b,c):
#     if(a>b and a>c):
#         print(f"{a} is greatest")
#     elif(b>c and b>a):
#         print(f"{b} is greatest")
#     else:
#         print(f"{c} is greatest")
# great(a,b,c)
# -----------------------------------
# c=int(input("enter the celcius"))
# def conv(c):
#     f=((c*9)/5)+32
#     return f
# g=conv(c)
# print(g)
# ---------------------------------------
# n=int(input("enter the number of N"))
# def sum(n):
#     s=n
#     if(n==1):
#         l=1
#     else:
#         s+=sum(n-1)
#         l=s
#     return l    
# r=sum(n)
# print(f"sum of natural numbers {r}")
# ----------------------------------------------
# n=int(input("enter the number of N"))
# for i in range(n,0,-1):
#     print("*"*i)
# ---------------------------------------------
# n=int(input("enter the number of INCHES"))
# c=n*2.54
# print(f"In centimeters:{c}")
# -----------------------------------------------
# n=int(input("enter no.:"))
# def mul(n):
#     for i in range(1,11):
#         c=i*n
#         print(f"{n}x{i}={c}")
# mul(n)
# -------------------------------------------------
# l=["v","a","r","s","h"]
# n=input("enter the element u wanna remove:")
# def f(l,n):
#     for i in l:
#         if n in l:
#             l.remove(n)
#             print(l)
#     else:
#         print("not found")
            
# f(l,n)
# ------------------------------------------------------
l=["varsha","aisja","rohan","shisha","hayat","an"]
n=input("enter the element u wanna remove:")
def term(l,n):
    m=[]
    for v in l:
        if not(v==n):
            m.append(v.strip(n))
    return m

print(term(l,n))