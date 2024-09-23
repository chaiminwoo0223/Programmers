# JadenCase 문자열 만들기
def solution(sentences):
    sentences = sentences.split(" ") # 공백을 유지하면서 단어를 나눈다.
    answer = []
    
    for sentence in sentences:
        if len(sentence) > 0 and sentence[0].isalpha(): # IndexError 방지
            sentence = sentence[0].upper() + sentence[1:].lower()
        else:
            sentence = sentence.lower()
        answer.append(sentence)
        
    return " ".join(answer)