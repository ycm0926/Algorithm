from collections import Counter

def solution(X, Y):
    X = sorted(Counter(X).items(),reverse=True)
    Y = sorted(Counter(Y).items(),reverse=True)
    X_K = [i[0] for i in X]
    Y_K = [i[0] for i in Y]
    X_V = [i[1] for i in X]
    Y_V = [i[1] for i in Y]
    res = []

    for i in X_K:
        if i in Y_K:
            res.append(i*min(X_V[X_K.index(i)],Y_V[Y_K.index(i)]))
    if not res:
        return '-1'
    elif sum(map(int,res)) == 0:
        return '0'
    else:
        return ''.join(res)