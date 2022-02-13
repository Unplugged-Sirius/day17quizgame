from question_model import questions
from data import question_data
from quiz_brain import QuizBrain
question_bank=[]
l=len(question_data)
for i in range (0,l):
 question_text=question_data[i]["text"]
 question_answer=question_data[i]["answer"]
 new_question=questions(question_text,question_answer)
 question_bank.append(new_question)
quiz=QuizBrain(question_bank)
while quiz.still_has_questions():
 quiz.next_question()
