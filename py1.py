lists = [1,4,5,7,9,8]

while True:
    ip = input("Enter 'q' to quit or Guess a number: ")

    if (ip == 'q'):
        break

    elif int(ip) in lists:
        print("You successfully guessed a number")

    else:
        print("Your guess is wrong")