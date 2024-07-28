# print("hello world")
print("When the blazing sun is gone,\nWhen he nothing shines upon,\nThen you show your little light,\nTwinkle, twinkle, all the night.\n\nThen the trav’ller in the dark,\nThanks you for your tiny spark,\nHe couldn’t see which way to go,\nIf you did not twinkle so.")
import pyjokes
j=pyjokes.get_joke()
print(j)
import os
p="C:\\Users\\Poornima\\Desktop\\python"
content=os.listdir(p)
for i in content:
    fp=os.path.join(p,i)
    print(fp)
    import pyttsx3
    e=pyttsx3.init()
    e.say("hello earth im varsha")
    e.runAndWait()
    