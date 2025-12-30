price = 1000000
cs = int(input("Enter your credit score in numbers: "))
age = int(input("Enter your age: "))
ten = price * 0.1
twenty = price * 0.2
if cs >= 600 and age >= 18: # comparison operator
    print("you have to make 10% down payment first which is ", ten)
elif cs < 600 or age >= 18: #there is also not operator 
    print("you have to make 20% down payment first which is ", twenty)
else:
    print("you are not eligible for loan")

# tasks

weight = float(input("Enter your weight: "))
type_of_input = input("(L)bs or (K)gs: ")
toi = type_of_input.lower()

if toi == "l":
    kg = float(weight) * 0.4536
    print(f"you are {kg} kilos")
else:
    lbs = float(weight) / 0.4536
    print(f"you are {lbs} pounds")