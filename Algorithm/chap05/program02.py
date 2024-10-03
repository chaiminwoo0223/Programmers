# 최소직사각형
def solution(sizes):
    width = 0 
    height = 0 
    
    for size in sizes:
        width = max(width, size[0], size[1])
        height = max(height, min(size[0], size[1]))
    return width * height
