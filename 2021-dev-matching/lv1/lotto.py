'''
- 모르는 번호는 0
- [최대등수, 최소등수] 출력

1. 현재 기준 최소 매칭 체크
2. 남은 0 개수, 중복없이 최대 매칭 가능 개수 체크?
'''
def solution(lottos, win_nums):
    answer = [0] * 2

    unknown = 0
    minn = 0

    for num in lottos:
        if num == 0:
          unknown += 1
        elif num in win_nums:
            minn += 1

    answer[0] = min(7 - (minn + unknown), 6)
    answer[1] = min(7 - minn, 6)

    return answer

solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19])