topic = input()
while True:
    guess = input()
    correct_positions = 0
    correct_digits = 0
    answer_dict = {}
    guess_dict = {}
    for i in range(4):
        if guess[i] == topic[i]:
            correct_positions += 1
        else:
            answer_dict[topic[i]] = answer_dict.get(topic[i], 0) + 1
            guess_dict[guess[i]] = guess_dict.get(guess[i], 0) + 1
    for digit, count in guess_dict.items():
        if digit in answer_dict:
            correct_digits += min(count, answer_dict[digit])
    if correct_positions == 4:
        print("You Win!")
        break
    print("{}A{}B".format(correct_positions, correct_digits))