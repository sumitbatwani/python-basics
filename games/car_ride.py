"""
    Use commands 
    help: to get instructions,
    start: to start a car,
    stop: to stop a car
    quit: to quit the game.
"""

print("Welcome to my car..")
started = False
while True:
    command = input("> ").lower()
    if command == "help":
        print(
            """
                start - to start a car
                stop - to stop a car
                quit - to quit the game
            """
        )
    elif command == "start":
        if started:
            print("Already started..")
        else:
            started = True
            print("car started..")
    elif command == "stop":
        if not started:
            print("Already stopped..")
        else:
            started = False
            print("car stopped")
    elif command == "quit":
        break
    else:
        print("I don't understand")
