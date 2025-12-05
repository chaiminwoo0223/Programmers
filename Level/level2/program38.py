# [3차] 파일명 정렬
# sorted(result, key=lambda x: (x[0].lower(), int(x[1])))
def solution(files):
    result = []

    for file in files:
        head, number, tail = "", "", ""
        check = False

        for i in range(len(file)):
            if file[i].isdigit():  # 처음 나오는 숫자부터 number
                number += file[i]
                check = True
            elif not check:  # number가 나오기 전까지는 head
                head += file[i]
            else:
                tail = file[i:]  # head, number가 모두 나왔다면 tail
                break

        result.append([head, number, tail])

    return ["".join(r) for r in sorted(result, key=lambda x: (x[0].lower(), int(x[1])))]
