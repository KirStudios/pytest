#setup
import random

def teachermode():
    global newq
    print("Hi! Welcome to Teacher Mode!")
    newq = int(input("How many questions?"))

def studentmode():
    questions_right = 0
    questions_wrong = 0
    for _ in range(newq):
        question_event = random.randint(0, 2) #0 is easy, 1 is mid, and 2 is hard
        if question_event == 0:
            n1 = random.randint(0, 10)
            n2 = random.randint(0, 10)
        elif question_event == 1:
            n1 = random.randint(10, 100)
            n2 = random.randint(10, 100)

        elif question_event == 2:
            n1 = random.randint(100, 1000)
            n2 = random.randint(100, 1000)

        op_event = random.randint(0, 3)

        op_type = ""

        if op_event == 0:
            answer = n1 + n2
            op_type = "+"

        elif op_event == 1:
            answer = n1 - n2
            op_type = "-"

        elif op_event == 2:
            answer = n1 * n2
            op_type = "*"

        elif op_event == 3:
            answer = n1 / n2
            op_type = "/"

        student_answer = input(f"Question {_}\nWhat is {n1} {op_type} {n2}?: ")
        #this if will be removed soon, this is just for testing
        if student_answer == "force":
            exec(f"global student_answer, n1, n2, op_type; student_answer = {n1} {op_type} {n2}")
        if student_answer == answer:
            print(f"Correct! {random.choices([':D', ':)', ';)', ';D'])}")
        else:
            print("wrong!")
studentmode()
input()