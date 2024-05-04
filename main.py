from data import question_data
from question_model import Question
from quiz_brain import Quizbrain
question_bank = []
for x in question_data:
     question_text = x["text"]
     question_answer = x["answer"]
     new_question = Question(question_text, question_answer)
     question_bank.append(new_question)

#print(question_bank)
quiz = Quizbrain(question_bank)

while quiz.still_has_questions():
     quiz.next_question()

print("You've completed the quiz")
print("/n")
print("Copyright Ken Magondu Chege")