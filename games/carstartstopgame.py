command=''
started=False
while command!='quit':
    command=input('> ').lower()
    if command=='help':
        print('start - to start the car')
        print('stop  - to stop the car')
        print('quit  - to exit the car')
    elif command=='start':
        if started:
            print("The car has already started! You don't need to start it again")
        else:
            print('The car has started!')
            started=True
    elif command=='stop':
        if not started:
            print('The car is already stopped!')
        else:
            print('The car has stopped')
            started=False
    elif command=='quit':
        print('Exiting the car')
        break
    else:
        print("I don't understand")
