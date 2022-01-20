testCases = [
    ("2-990-5+2", 300)
]
from itertools import permutations
from copy import deepcopy


def get_numbers_and_exps(expression): # 수식을 숫자와 연산자 배열로 분리
    exps = []
    numbers = []
    # 수식 분석
    start_num_idx = 0  # 숫자의 시작을 저장할 index
    for i in range(len(expression)):
        if not expression[i].isdigit():  # i번째 문자가 연산 문자인 경우
            numbers.append(expression[start_num_idx:i])  # start~i-1번째까지 slice하여 숫자 배열에 추가
            exps.append(expression[i])  # i번째는 연산문자 배열에 추가
            start_num_idx = i + 1  # 다음 숫자 시작 index는 i+1
    numbers.append(expression[start_num_idx:])  # for문이 끝나고 난후 마지막 숫자를 숫자 배열에 추가
    return numbers, exps


def calc(numbers, exps, exp_seq):
    for exp in exp_seq:
        before_exp_used = False # 이전에 수식어가 계산을 했는지 안했는지 여부 저장
        new_nums_tmp = [] # 계산 후의 숫자 저장
        for i, num in enumerate(numbers):
            if i == len(numbers) - 1: # 마지막 num의 경우
                if not before_exp_used: # 이전의 수식어가 사용되지 않았다면
                    new_nums_tmp.append(num) # 새로운 숫자 배열에 추가
                break

            if exp == exps[i]: # 현재 우선순위의 연산자를 만난 경우
                sub_result = str(eval(numbers[i] + exp + numbers[i + 1])) # i, i+1번째 숫자로 계산
                numbers[i + 1] = sub_result # numbers[i+1]에 계산 결과 저장
                if before_exp_used: # 이전에 계산을 한 경우(현재 우선순위의 연산자가 연속으로 나온 경우)
                    new_nums_tmp[-1] = sub_result # 마지막에 저장된 숫자를 갱신함
                else:
                    new_nums_tmp.append(sub_result) # 이전에 계산을 하지 않은 경우 새로운 숫자 배열에 추가
                before_exp_used = True
            else:
                if not before_exp_used: # 이전에 계산을 하지 않은 경우
                    new_nums_tmp.append(num) # 새로운 숫자배열에 숫자만 추가
                before_exp_used = False

        numbers = new_nums_tmp.copy() # new_nums로 배열 갱신
        exps = [e for e in exps if e != exp] # 이전 연산자를 제외한 연산자만 남도록 갱신

    return abs(int(numbers[0])) # 절댓값 반환


def solution(expression):
    ret = 0

    numbers, exps = get_numbers_and_exps(expression)

    # 순열을 이용하여 모든 경우 탐색
    for exp_seq in permutations(list(set(exps))):
        # exp_seq에서 우선순위 별로 하나씩 문자를 가져옴
        ret = max(ret, calc(numbers.copy(), exps.copy(), exp_seq))
    return ret
