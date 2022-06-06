
flag_started=False

while True:
    user_command = input('>').lower()
    if user_command =='help':
           print("""
start - for starting the car
stop - stop the car
quit  - quit the game
""")
    elif user_command =='start':
        if not flag_started:
          print('Car started!')
          flag_started=True
        else:
          print('Car is already started')
    elif user_command == 'stop':
           print('Car stopped')
           flag_started = False
    elif user_command == 'quit':
        break
    else:
          print("I don't understand")



