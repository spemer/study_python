import random, getUserInfo, getAns

print ("%s님 환영합니다.\n" % getUserInfo.getUserId())


def main():
    _WRONG = 0
    _PROCESS = 0
    _POINT = 100
    grade = ""


    strDict = ["apple", "peach", "banana", "melon", "cake", "coffee", "bread", "chocolate"]
    q_data = random.choice(strDict)

    print("선택한 단어의 글자수는 %d 개 입니다.\n" % len(q_data))
    getAns.findWord(q_data)


    while (_PROCESS >= 0):
        Ans_Data = input("답을 입력하세요: ")

        if Ans_Data == q_data:
            _PROCESS = _PROCESS - 1
            print("정답입니다.")

        else:
            print("입력한 글자는 틀렸습니다.\n")
            _WRONG = _WRONG + 1
            getAns.findWord(q_data)


    _POINT = _POINT - (_WRONG * 10)

    if (_POINT >= 90):
        grade = '"Good"'
    elif (_POINT >= 50):
        grade = '"Not Bad"'
    elif (_POINT >= 20):
        grade = '"Bad"'



    print("\n==========\n")
    print("당신의 포인트는 %d점 입니다.\n당신의 수준은 %s입니다." % (_POINT, grade))




main()