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


#결과 보여주기
def scoreIs_Final (correct, myScore, grade) :
    print("\n==========\nResult\n")
    print("Correct: %d\nScore:   %d\nGrade:   %s" % (correct, myScore, grade),
          "\n==========\n")

