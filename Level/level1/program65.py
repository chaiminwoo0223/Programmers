# [PCCE 기출문제] 10번 / 데이터 분석
def solution(data, ext, val_ext, sort_by):
    result = [x for x in data if (ext == "code" and x[0] < val_ext) or
              (ext == "date" and x[1] < val_ext) or
              (ext == "maximum" and x[2] < val_ext) or
              (ext == "remain" and x[3] < val_ext)]

    if sort_by == "code":
        return sorted(result, key=lambda x: x[0])
    elif sort_by == "date":
        return sorted(result, key=lambda x: x[1])
    elif sort_by == "maximum":
        return sorted(result, key=lambda x: x[2])
    else:
        return sorted(result, key=lambda x: x[3])
