#LOOP PRACTICE EXAMPLE PYTHON
command = ""
hasStarted = False
hasStopped = True
while True:
    command = input('>').lower()
    if command == 'start' and hasStarted is False:
        print('Car has started')
        hasStopped = False
        hasStarted = True
    elif command == 'start' and hasStarted is True:
        print('Car is already running')
    elif command == 'stop' and hasStopped is False:
        print('Car has stopped')
        hasStarted = False
        hasStopped = True
    elif command == 'stop' and hasStopped is True:
        print('Car is already idle')
    elif command == 'help':
        print("""
start for starting
stop for stopping
quit for exit
        """)
    elif command == 'quit':
        break;
    else:
        print('I do not understand the command')