import correct_func

ANSWER = [1,2,3,1,2,3,1,2,3,1]

def main():
    My_ANSWER =    correct_func.InMyAns ()
    myScore = (    correct_func.score (correct_func.correct (ANSWER, My_ANSWER) ))



    correct_func.scoreIs_Final\
            (
        My_ANSWER,
        correct_func.correct (ANSWER, My_ANSWER), # 정답
        myScore,                                  # 점수
        correct_func.grade (myScore),             # 등급
    )

    correct_func.getMoreStudents(My_ANSWER)

main()