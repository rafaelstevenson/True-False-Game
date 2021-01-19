import art
print("Welcome to the True/False game !")
print(art.logo)
print(art.description)
play_game = True
while play_game==True:
    print(art.topic_list)

    from question_model import Question
    from data import question_data
    from quiz_brain import QuizBrain

    question_bank = []
    print("Okay, here we go!\n")
    for question in question_data:
        question_answer = Question(question['question'], question['correct_answer'])
        question_bank.append(question_answer)

    quiz = QuizBrain(question_bank)

    while quiz.still_has_question():
        quiz.next_question()

    quiz.finish_quiz()
    play_again = input("Do you want to play again(y/n)? ")
    if play_again == 'n':
        play_game = False
