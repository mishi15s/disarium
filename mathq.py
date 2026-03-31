import random
op=["+","*","-"]
correct=0
score=0
q=0
print("Welcome to the maths quiz✖️  ➕ ➖ ➗ 📃 🔢")
while q<5:
    num1=random.randint(0,50)
    num2=random.randint(0,50)
    opera=random.choice(op)
    print(f"What is {num1}{opera}{num2}?")
    ans=int(input("Enter the answer:"))
    if opera=="+":
        correct=num1+num2
    elif opera=="-":
        correct=num1-num2
    elif opera=="*":
        correct=num1*num2
    if ans==correct:
        print("Correct answer")
        score=score+1
        
    else:
        print("Wrong answer")
        print(f"The correct answer is {correct}")
    q=q+1
print(f"Score:{score}/5")
if score==5:
    print("🏆🏆🏆🏆Congratulations!A perfect score!🏆🏆🏆🏆")