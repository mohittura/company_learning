#while loop
i = 1
while i<=5:
    print('*' * i)
    i+=1
print("done")

# guessing game

answer = 9
limit = 3
count = 0
while count < limit:
    guess = int(input("Guess the number: "))
    count += 1
    if guess == answer:
        print("you won")
        break # to break the loop
else:
    print("you failed")

# for loop

prices = [10,20,30]
total = 0
for price in prices:
    total += price  
print(total)

