def embed(first_name, last_name):
    message = input(f"how was your day? {first_name} {last_name} ")
    words = message.split(' ')
    emojis ={
        ":)": "😄",
        ":(": "😞"
    }
    out = ""
    for word in words:
        out += emojis.get(word,word) + " "
    print(out)

embed(last_name="Manglani", first_name="Mohit") # keyword arguements



#return 
def square(number):
    square_num = number * number 
    return square_num

answer = square(10)
print(answer)