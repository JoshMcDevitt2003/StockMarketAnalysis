def Question1(answer1):
    answercount1 = 0
    if answer1 == "A":
        answercount1 += 1
    return answercount1
def Question2(answer2):
    answercount2 = 0
    if answer2 == "C":
        answercount2 += 1
    return answercount2
def Question3(answer3):
    answercount3 = 0
    if answer3 == "B":
        answercount3 += 1
    return answercount3
def Question4(answer4):
    answercount4 = 0
    if answer4 == "A":
        answercount4 += 1
    return answercount4
def Question5(answer5):
    answercount5 = 0
    if answer5 == "C":
        answercount5 += 1
    return answercount5
playagain = "Yes"
while playagain == "Yes":
    print("A. Tr(A^*B)")
    print("B. (A-I)B")
    print("C. AB")
    answer1 = input("What is the inner product of two matrices (A,B) under the standard Frobenius inner product?")
    result1 = Question1(answer1)
    print("A. f: R --> R^2")
    print("B. f: R --> R")
    print("C. f: R --> [-pi/2,pi/2]")
    answer2 = input("Which of the following is an injection under the function f(x) = arctan(x)?")
    result2 = Question2(answer2)
    print("A. a^3+b^3")
    print("B. 1")
    print("C. 0")
    answer3 = input("How many vectors exist that model the functional f: R^2 --> R f(<a,b>)=a^2+b^2 in the form of an inner product?")
    result3 = Question3(answer3)
    print("A. infinite")
    print("B. less than 100")
    print("C. 0")
    answer4 = input("Given an infinetly differentialbe function trigonomic G how many non zero terms are in the taylor series expansion?")
    result4 = Question4(answer4)
    print("A. 3N")
    print("B. N^2")
    print("C. 0")
    answer5 = input("Given a N demnetional vector space H how many subspaces of H exist with a demnetion greater than N?")
    result5 = Question5(answer5)
    finalresult = result1 + result2 + result3 + result4 + result5
    print("Your Score:", finalresult)
    playagain = input("Do you want to take the quiz again?:")