name=input("enter your name:")
print("Good morning"+" "+name)
print(f"gm  {name}")
letter="""Dear <|name|>
            you are selected!
            <|date|>"""
print(letter.replace("<|name|>","varsha").replace("<|date|>","24 march 2024"))
l=name.count("  ")
if(l==0):
   print("none")
else:
    n=name.find("  ")
    print(n)
    print(name.replace("  "," "))

