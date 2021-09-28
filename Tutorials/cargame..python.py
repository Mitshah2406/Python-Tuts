print("            THE CAR GAME           ")
print("Type 'help' to get information about all commands related to this game.")
command = ""
started = False
while command != "quit":
    command = input('> ').lower()
    if command == "start":
        if started:
            print("The Car is already started.")
        else:
            started = True
            print("The Car started.")
    elif command == "stop":
        if not started:
            print("The Car has already stopped.")
        else:
            started = False
            print("The Car stopped.")
    elif command == "help":
        print("""
start - to start the car.
stop - to stop the car.
quit - to quit.
        """)
    elif command == "quit":
        print("Thanks for playing the game.")
        break
    else:
        print("Sorry,I don't understand this.")
