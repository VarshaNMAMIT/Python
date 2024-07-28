# n=int(input("enter no.:"))
# for i in range(1,11):
#     c=i*n
#     print(f"{n}x{i}={c}")
# -------------------------------
# l=["harr","soh","sac","rah"]
# for li in l:
#     if (li.startswith('s')):
#         print(f"hello{li}")
# ----------------------------------
# n=int(input("enter no.:"))
# i=1
# while (i<11):
#     c=i*n
#     print(f"{n}x{i}={c}")
# #     i+=1
# # --------------------------------
# n=int(input("enter no.:"))
# i=2
# p=n**0.5
# print(p)
# while i<=p:
#     if(n%i==0):
#         print("not a prime")
#         exit(0)
#     i=i+1
# print("prime number")
# -------------------------------------
# n=int(input("enter no.:"))
# s=input("enter numbers seperated by space:")
# l=s.split(" ")
# i=0
# sum=0
# while i<n:
#     sum+=int(l[i])
#     i+=1
# print(f"total sum is {sum}")
# -----------------------------
# n=int(input("enter no.:"))
# f=n
# for i in range(1,n):
#     f*=i
# print(f"factorial of {n} is :{f}")
# ----------------------------------
# n=int(input("enter no.:"))
# l=[]
# for i in range(1,n*2,2):
#     l.append(i)
# for m in l:
#     print("*"*m)
# ---------------------------------
# for i in range(0,n):
#     print("*"*(i+1))
# --------------------------------
# n=int(input("enter no.:"))
# for i in range(1,n+1):
#     if(i%2==0):
#         print("* *")
#     else:
#         print("*"*3)
# --------------------------------
# n=int(input("enter no.:"))
# for i in range(10,0,-1):
#     c=i*n
#     print(f"{n}x{i}={c}")
# --------------------------------
n=int(input("enter no.:"))
for i in range (1,n+1):
    print(" "*(n-i),end="")
    print("*"*(2*i-1),end="")
    print(" "*(n-i))




















