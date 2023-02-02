def solution(id_list, report, k):
    answer = {}
    report_dic ={}

    for i in range(len(id_list)):                   # 나를 신고한 명단 딕셔너리와 횟수 카운트 딕셔너리 만듦 
        report_dic[id_list[i]] = []
        answer[id_list[i]] = 0
    for i in report:
        a,b = i.split()                             # 이용자와 신고자 스플릿
        if a not in report_dic[b]:
            report_dic[b] += [a]                    # 예를 들어, a가 b를 신고한 경우 b의 value에 추가

    for i in report_dic.values():                   # 정지가 성공한 횟수 카운트
        if len(i) >= k:                             # k이상이여서 정지가 성공했다면
            for j in i:                             # 신고한 유저들 +1
                answer[j] += 1
    return list(answer.values())