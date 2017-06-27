def findWord(q_data):
    Ans = input("찾을 글자를 입력하세요: ")

    count = 0
    for ch in q_data:
        if ch == Ans:
            count += 1

    print("%s 는 단어안에 %d개 있습니다.\n" % (Ans, count))