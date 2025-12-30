try:
    age = int(input("Age: "))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print("Enter a number not anything else")
except ZeroDivisionError:
    print("invalid number (division by zero)")

