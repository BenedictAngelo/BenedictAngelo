questions = ["What is the color of the sun? ", "What is the color of the ocean? ", "What is the color of the sky? "]
choices = ["A. Yellow", "B. Blue", "C. Red", "D. Sky Blue"]
correct = ["A", "B", "D"]
answers = []
score = 0
quest_num = 0
for items in questions:
    print(items)
    for each in choices:
        print(each)
    answer = input("Answer: ").upper()
    answers.append(answer)
    if answers[quest_num] == correct[quest_num]:
        print("Correct")
        quest_num += 1
        score += 1 
    else:
        print("Wrong")
   # print(answers)
print(f"Your score is: {score}")

if score == 3:
    print("Perfect")
else:
    print("Try harder")
