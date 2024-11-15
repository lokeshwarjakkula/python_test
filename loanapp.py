age = int(input("Please enter your age: "))

if age>=18 and age<=30:
    print("Welcome")
    salary = int(input("Please enter your salary: "))

    if salary >= 30000:
        print("You are eligible for a loan up to 40%")
    elif 20000 < salary <= 30000:
        print("You are eligible for a loan up to 20%")
    else:
        print("Not eligible for a loan")

elif age>=30 and age<=40:
    print("Welcome")
    salary = int(input("Please enter your salary: "))

    if salary>50000:
         print("You are eligible for a loan up to 60%") 
    elif 30000 < salary <= 50000:
        print("You are eligible for a loan up to 50%")
    elif 20000 < salary <= 30000:
        print("You are eligible for a loan up to 20%")
    else:
        print("Not eligible for a loan")
else:
    print("You don't meet the age limit")