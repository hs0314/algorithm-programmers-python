'''
- 한번에 한 명 신고 가능(횟수제한X, 다른 유저 신고 가능)
- 한 유저의 신고횟수는 1회로 고정
- k번 이상 신고 시 이용정지 -> 신고한 유저에게 메일 발송

=> id_list 순서대로 각 유저가 받는 메일 수 출력

*** sol
1. 각 name을 key로 하는 신고한 사람 list dict 생성
2. k를 넘는 name인 경우, answer list의 신고한 사람 idx에 +1
'''
def solution(id_list, report, k):
    answer = [0 for i in range(len(id_list))] # 크기가 있는 list 0 초기화
    # answer = [0] * len(id_list)

    report_info = {} # name : 본인을 신고한사람list

    #1
    for row in report:
        sub, obj = row.split(" ")[0], row.split(" ")[1]

        if obj in report_info:
            report_info[obj].add(sub)
        else:
            report_info[obj] = {sub}


    #2
    for idx, id in enumerate(id_list):
        if id in report_info and len(report_info[id]) >= k:

            for sub in report_info[id]:
                answer[ id_list.index(sub) ] += 1

    return answer



solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3)