print('welcome to the simple quiz game')
# This script starts a simple quiz game by welcoming the user.
print('Are you ready to play?')
user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Let's start the quiz.")
# This script prompts the user for their name and confirms their readiness to play the quiz game.
print('Good luck!')
# This script provides a simple quiz game introduction and prompts the user for their name.
Question_number = input("Enter the number of questions you want to answer: ")
print(f"You have chosen to answer {Question_number} questions.")
# This script prompts the user for the number of questions they want to answer in the quiz game.
print('Let\'s begin the quiz!') # This script indicates the start of the quiz after the user has chosen the number of questions.
print('Please answer the following questions:')
# This script prompts the user to start answering the quiz questions after the initial setup.
Question_1 = print('Question 1: What is the capital of France?')
# This script presents the first question of the quiz game to the user.
print('A) Paris')
print('B) London')
print('C) Berlin')
# This script provides multiple-choice options for the first question of the quiz game.
answer1 = input("Your answer (A/B/C): ")
if answer1.upper() == 'A':
    print("Correct! Paris is the capital of France.") # This script checks the user's answer to the first question and confirms if it is correct.
else:
    print("Incorrect. The correct answer is A) Paris.") # This script informs the user if their answer to the first question is incorrect and provides the correct answer.
Question_2 = print('Question 2: What is 2 + 2?') # This script presents the second question of the quiz game to the user.
print('A) 3')
print('B) 4')
print('C) 5')
answer2 = input("Your answer (A/B/C): ")
if answer2.upper() == 'B':
    print("Correct! 2 + 2 equals 4.") # This script checks the user's answer to the second question and confirms if it is correct.
else:
    print("Incorrect. The correct answer is B) 4.")
Question_3 = print("Who is the president of Nigeria?") # This script presents the third question of the quiz game to the user.
print('A) Goodluck Jonathan')
print('B) Muhammadu Buhari')
print('C) Bola Ahmed Tinubu')  
answer3 = input("Your answer (A/B/C): ")
if answer3.upper() == 'C':
    print("Correct! Bola Ahmed Tinubu is the current president of Nigeria.") # This script checks the user's answer to the third question and confirms if it is correct.
else:
    print("Incorrect. The correct answer is C) Bola Ahmed Tinubu.")
print("Thank you for playing the quiz game!") # This script thanks the user for participating in the quiz game.
if Question_1 == "A" and Question_2 == "B" and Question_3 == "C":       
    print("Congratulations! You answered all questions correctly!") # This script congratulates the user for answering all quiz questions correctly.
else:
    print("You answered some questions incorrectly.") # This script informs the user that they did not answer all quiz questions correctly. Ab
