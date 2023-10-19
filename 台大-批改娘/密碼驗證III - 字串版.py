password = input()
while True:
    guess = input()
    if guess == password:
        print("Correct!")
        break
    else:
        print("Wrong Password!")
        continue