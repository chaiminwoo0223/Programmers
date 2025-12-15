# 키패드 누르기
# 인덱스
def solution(numbers, hand):
    result = ""
    hands = {"left": "*", "right": "#"}
    lefts = [1, 4, 7, "*"]
    middles = [2, 5, 8, 0]
    rights = [3, 6, 9, "#"]

    for number in numbers:
        if number in lefts:
            hands["left"] = number
            result += "L"
        elif number in rights:
            hands["right"] = number
            result += "R"
        else:
            left = hands["left"]
            right = hands["right"]
            m = middles.index(number)

            if left in lefts:
                l = lefts.index(left)
                left_distance = abs(m - l)
            else:
                l = middles.index(left)
                left_distance = abs(m - l) - 1

            if right in rights:
                r = rights.index(right)
                right_distance = abs(m - r)
            else:
                r = middles.index(right)
                right_distance = abs(m - r) - 1

            if left_distance < right_distance:
                hands["left"] = number
                result += "L"
            elif left_distance > right_distance:
                hands["right"] = number
                result += "R"
            else:
                if hand == "left":
                    hands["left"] = number
                    result += "L"
                else:
                    hands["right"] = number
                    result += "R"

    return result
