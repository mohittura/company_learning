ui = ""

while True:
    ui = input("> ").lower()
    if ui == "start":
        print("Car started... ready to go")
    elif ui == "stop":
        print("Car stopped")
    elif ui == "quit":
        break
    else:
        print("i dont understand that")