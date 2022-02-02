command = ""
started = False

while command != 'quit':
    command = input('> ').lower()


    if command == 'start':
        if started:
            print("Hey car already started...")
        else:
            started = True
            print("Car started...")


    elif command == 'stop':
        if not started:
            print("Car already stopped...")
        else:
            started = False
            print("car stopped...")


    elif command == 'help':
     print("start - to start the car")
     print("stop - stop the car")
     print("quit- to exit")

    elif command == "quit":
        print("Terminated..")
        break

    else:
        print("i don't understand")
