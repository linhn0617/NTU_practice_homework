password = int(input())
while True:
    if password <= 0 or password >= 2000000000 :
        print("Wrong Password Setting!")
        break
    else:
        guess = int(input())
        if guess == password:
            print("Correct!")
            break
        else:
            print("Wrong Password!")
            continue