command = ''
started = False
fuel = 5
speed = 0

print("Car Simulator 3.0 - Ready to roll!")

while command != 'quit':
    command = input('> ').lower()
    
    if command == 'help':
        print('start  - Start engine')
        print('stop   - Stop engine')
        print('drive  - Increase speed (uses fuel)')
        print('refuel - Fill the tank (must be stopped)')
        print('quit   - Exit')
        
    elif command == 'start':
        if started:
            print("The engine is already humming!")
        else:
            print('Engine started! Ready to drive.')
            started = True
            
    elif command == 'stop':
        if not started:
            print('The engine is already off.')
        else:
            print('Engine stopped.')
            started = False
            speed = 0  # Car resets to 0 speed when stopped
            
    elif command == 'drive':
        if not started:
            print("You can't drive with the engine off!")
        elif fuel <= 0:
            print("You're out of gas! Better refuel.")
        else:
            fuel -= 1
            speed += 10
            print(f"Vroom! You're going {speed} km/h. Fuel left: {fuel}")
            
    elif command == 'refuel':
        if started:
            print("Safety warning: You cannot refuel while the engine is running!")
        else:
            fuel = 5
            print("Tank full! Ready to hit the road.")
            
    elif command == 'quit':
        print('Exiting the car...')
        break
    else:
        print("I don't understand")