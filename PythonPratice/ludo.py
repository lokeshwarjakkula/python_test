
import random
human = int(input("Please enter your number : "))
system=random.randint(1,6)
print("system",system)
print("human",human)
if human>=1 and human<=6:
   if human>system:
    print("human win")
   elif system>human:
    print("system win")
   else:
    print("both or equal draw")    
else:
    print("invaild number entered")
