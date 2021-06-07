def new_game():

    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (a, b, c, or d): ")
        guess = guess.lower()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")


def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False



questions = {
 "Which was the largest site of Indus Civilization? ": "a",
 "What year was Python created?: ": "b",
 "Who was the founder of Indian National Congress?: ": "b",
 "Is the Earth round?: ": "a"
}

options = [["a Mohenjodaro,b Lothal,c Chanhudaro,d Dholavira"],
          ["a. 1989", "b. 1991", "c. 2000", "d. 2016"],
          ["a Gopal Krishna Gokhle,b Allen Octavian Hume,c Feroz Shah Mehta,d Bipin Chandra Pal"],
          ["a. True","b. False", "c. sometimes", "d. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!")
