import question
import data
import quiz_brain as qb

question_bank=[]

for q in data.question_data:
    question_bank.append(question.Question(q["text"], q["answer"]))

quiz=qb.QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed the quiz.")
print(f"Your final score is:{quiz.score}/{quiz.question_number} ")