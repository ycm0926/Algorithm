def solution(a, b):
    mon = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day = {1:'FRI',2:"SAT",3:'SUN',4:'MON',5:"TUE",6:'WED',0:'THU'}
    res = b
    for i in mon[:a-1]:
        res += i
    return day[res%7]