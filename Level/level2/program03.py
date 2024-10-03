# JadenCase 문자열 만들기
# '': 빈 문자열 vs ' ': 공백 문자
def solution(sentences):
    sentences = sentences.split(' ') # 공백을 유지하면서 단어를 나눈다.(문자열 -> 리스트)
    result = []
    
    for sentence in sentences:
        if sentence == '':
            result.append(sentence)  
        elif sentence.isalpha():
            result.append(sentence[0].upper() + sentence[1:].lower())
        else:
            result.append(sentence.lower())
            
    return " ".join(result)
