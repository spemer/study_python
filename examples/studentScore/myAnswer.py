import correct_func

ANSWER = [1,2,3,1,2,3,1,2,3,1]
getStudentNumb = int(input("Number of students: "))
print()

# def _main(getStudentNumb):
#     return main(getStudentNumb)

def main(getStudentNumb):
    STUDENT = []

    for i in range(0, getStudentNumb) :
        STUDENT.append(i)
        print ("Student %d" % len(STUDENT))


        My_ANSWER = correct_func.InMyAns()
        myScore   =(correct_func.score (correct_func.correct (ANSWER, My_ANSWER) ))


        correct_func.scoreIs_Final\
                (
            correct_func.correct (ANSWER, My_ANSWER), # 정답
            myScore,                                  # 점수
            correct_func.grade (myScore)              # 등급
        )



main(getStudentNumb)