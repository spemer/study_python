#맞은 개수
def correct (ANSWER, My_ANSWER) :
    count = 0
    for i in range  (0, len(ANSWER)):
        if ANSWER [i] == My_ANSWER[i]:
            count += 1
    return  count


#점수 구하기
def score (yourScore) :
    return yourScore * 10


#등급 구하기
def grade (myScore) :
    if     myScore >= 90: _grade = 'A'
    elif   myScore >= 80: _grade = 'B'
    elif   myScore >= 70: _grade = 'C'
    elif   myScore >= 60: _grade = 'D'
    else:                 _grade = 'F'
    return                _grade


#답 입력받기
def InMyAns () :
    GET_ANSWER = []
    IPT_ANSWER = 0
    for i in range (0, 10):
        print("No.", i + 1, "Answer: ", end="")
        IPT_ANSWER = int(input())
        GET_ANSWER.append(IPT_ANSWER)

    return GET_ANSWER


# 학생 수
def _studentNumb(My_ANSWER):
    studentNumb = 0

    if len(My_ANSWER) == 10 :
        studentNumb += 1

    print ("\nStudent number %d" % studentNumb)


#결과 보여주기
def scoreIs_Final (My_ANSWER, correct, myScore, grade) :
    studentNumb = 0

    if len(My_ANSWER) == 10 :
        studentNumb += 1

    print("\n==========\nResult of Student %d\n" % studentNumb)
    print("Correct: %d\nScore:   %d\nGrade:   %s" % (correct, myScore, grade),
          "\n==========\n")


#학생 더 입력받기
def getMoreStudents (My_ANSWER) :
    _getMoreStudents = input("Do you want to input more students answer? Y/N: ")

    COUNT = 0
    STUDENT = []

    while _getMoreStudents == "Y" or _getMoreStudents == "y" :


        for i in range (0, COUNT) :
            STUDENT.append(_studentNumb(My_ANSWER))

            print (STUDENT[i])
