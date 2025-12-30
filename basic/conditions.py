# if elif statement
weather = input("Is the day Hot, Cold or Warm: ")
ans = weather.lower()
if ans == "hot":
    print("the day is hot")
elif ans == "cold":
    print("the day is cold")
else:
    print("the day is warm")


# if else statement

age = int(input("What is your age: "))
if age >= 18:
    print("you are eligible to vote")
else:
    print("you are not eligible to vote")

# task 

price = 1000000
cs = int(input("Enter your credit score in numbers: "))
ten = price * 0.1
twenty = price * 0.2
if cs >= 600:
    print("you have to make 10% down payment first which is ", ten)
else:
    print("you have to make 20% down payment first which is ", twenty)