# 오픈채팅방
# 채팅방은 중복 닉네임을 허용
# 첫 단어는 Enter, Leave, Change 중 하나
# Leave한 사람이 다시 안 들어오는 경우 제외
def solution(record):
    result = []
    nicknames = {}

    for r in record:
        command = r.split()

        if command[0] == "Enter":
            result.append(command[1] + "님이 들어왔습니다.")

        if command[0] == "Leave":
            result.append(command[1] + "님이 나갔습니다.")

        if command[0] in ("Enter", "Change"):
            nicknames[command[1]] = command[2]

    for i, r in enumerate(result):
        user = r[:r.index("님")]
        result[i] = r.replace(user, nicknames[user])

    return result