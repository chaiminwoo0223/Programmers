# 신규 아이디 추천
def solution(new_id):
    result = ''

    # 1단계, 2단계
    for n in new_id.lower():
        if n.isalpha() or n.isdigit() or n in ['-', '_', '.']:
            result += n

    # 3단계
    while '..' in result:
        result = result.replace('..', '.')

    # 4단계
    if result and result[0] == '.':
        result = result[1:]

    if result and result[-1] == '.':
        result = result[:-1]

    # 5단계
    if not result:
        result = 'a'

    # 6단계
    if len(result) > 15:
        result = result[:15]

        if result[-1] == '.':
            result = result[:-1]

    # 7단계
    while len(result) < 3:
        result += result[-1]

    return result