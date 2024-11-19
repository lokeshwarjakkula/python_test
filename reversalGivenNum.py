a=int(input("enter your number"))
result=0
while a>0:
  last=a%10
  result=result*10+last
  a=a//10
print("reversal number ",result)
