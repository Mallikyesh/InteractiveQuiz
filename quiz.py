print("welcome to the quiz show\n \n \n we are super excited to throw some mind boggling questions and dare you to score and win\n")
print("each question carries 1 point and you will have 5 questions to face.")

points=int(0)

QUESTIONS = [
    ("When was the first known use of the word 'quiz'", "1781", "18th century"),
    ("Which built-in function can get information from the user", "input" , ""),
    ("Which keyword do you use to loop over a given list of elements", "for", "while"),
    ("Which key do you use to give a blank space ", "space", "blank"),
    ("Where is Afghanisthan located (continent)","Asia","asia"),
]

for questions, correct_answers, alt_ans in QUESTIONS:
    answer=input(f"{questions}? ")
    if answer==correct_answers or answer==alt_ans:
        print("Correct!")
        points=points+1
    else:
        print(f"False \nThe answer is {correct_answers !r}")

sentence="your final score is %d out of 5" %points    
print(sentence)
