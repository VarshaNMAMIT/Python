# f=open("file.txt","r")
# data=f.read()
# print(f"following is content of given file{data}")
# f.close()
# f=open("file.txt","w")
# f.write("trees are green ,tea is green and chocolate too??")
# f.close()
# f=open("file.txt","a")
# f.write(" Hello earth this is vars")
# f.close()
# --------------------------------------------------------------
# v=False
# with open("poems.txt") as f:
#     lines=f.readlines()
#     for line in lines:
#         if "twinkle" in line:
#             v=True
# if v :
#     print("found")
# else:
#     print("not")
# ------------------------------------------------------------
# import random
# def game():
#     print("you are playing a luck game")
#     s=random.randint(1,60)
#     print(f"your score is: {s}")
#     return s
# p=game()
# f=open("file.txt")
# high=f.read()
# hi=int(high)
# f.close()
# print(f"high till now is:{high}")
# if p>hi:
#     print("yours is the new high")
#     f=open("file.txt","w")
#     f.write(str(p))
#     f.close()
# else:
#     print("yours is less than high score")
# -------------------------------------------------
# def table(i):
#     with open(f"table of {i}.txt","w") as f:
#         t=""
#         for j in range(1,11):
#             t+=f"{i}x{j}={i*j}\n"
#         f.write(t)


# for i in range(1,21):
#     table(i)
# ------------------------------------------------------
# file=input("enter the file name :")
# with open(f"{file}","r") as f:
#     data=f.read()
# c=data.replace("donkey","###")
# with open(f"{file}","w") as f:
#     f.write(c)
# --------------------------------------------------------
# file=input("enter the file name :")
# l=["too","the","is"]
# with open(f"{file}","r") as f:
#     data=f.read()
# for m in l:
#     data=data.replace(m,"**")#putting c=this will replace only list last term not others
# with open(f"{file}","w") as f:
#     f.write(data)
# ------------------------------------------------------------------------
# file="log.txt"
# with open(file,"r") as f:
#     for line in f:
#         if "python" in line.lower():
#             print("present remove it")
#     else:
#         print("not present")
# ---------------------------------------------------------------------
# file="log.txt"
# with open(file) as f:
#     li=0
#     for line in f:
#         li+=1
#         if "python" in line.lower():
#             print(f"present in line {li}")
#             break
#     else:
#         print("not present")
# ---------------------------------------------------------------------
# o="log.txt"
# with open(o,"r") as f:
#     c=f.read()
# with open("new.txt","w") as f:
#     f.write(c)
# -------------------------------------------------------------------------
# with open("log.txt") as f:
#     c1=f.read()
# with open("new.txt") as f:
#     c2=f.read()
# if c1==c2:
#     print("yes identical")
# else:
#     print("not identical")
# --------------------------------------------------------------
# with open("new.txt","w") as f:
#      c2=f.write("")
# --------------------------------------------------
#rename is by copying content from 1 file to other and delete first one






    
    


        



    