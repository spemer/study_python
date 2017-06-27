matrix = []


numb_rows = int(input("행의 개수: "))
numb_cols = int(input("열의 개수: "))


for row in range (0, numb_rows) :
    matrix.append([])
    for col in range (0, numb_cols):
        value = int(input("원소를 입력하고 엔터를 누르세요: "))
        matrix[row].append(value)


print(matrix)




for row in range (0, len(matrix)) :
    for col in range (0, len(matrix[row])):
        print (matrix[row][col], end=" ")
    print()




total = 0
for row in (0, len(matrix) + 1) :
    for col in (0, len(matrix[col]) + 1) :
        total = matrix[row][col] + total

print(total)





maxRow = sum(matrix[0])
indexOfMaxRow = 0
for row in range (1, len(matrix)) :
    if sum (matrix[row]) > maxRow :
        maxRow = sum(matrix[row])
        indexOfRow = row

print(indexOfMaxRow, "번째 행의 합계", maxRow, "가 가장 큽니다")