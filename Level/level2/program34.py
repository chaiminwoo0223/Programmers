# 스킬트리
# 너무 어렵게 생각하지마!
def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        order = ""

        for s in skill_tree:
            if s in skill:
                order += s

        if skill[:len(order)] == order:
            answer += 1

    return answer