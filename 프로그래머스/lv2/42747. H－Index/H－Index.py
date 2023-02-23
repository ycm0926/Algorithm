def solution(citations):
    ci = sorted(citations, reverse= True)
    
    for i in range(len(ci)):
        if ci[i] <= i:
            return i
    return len(ci)