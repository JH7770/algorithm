
testCases = [
    ("2-990-5+2",300)
]
from itertools import permutations
from copy import deepcopy

def solution(expression):
    exps = []
    numbers = []

    start_num_idx = 0

    ret = 0
    for i in range(len(expression)):
        if not expression[i].isdigit():
            numbers.append(expression[start_num_idx:i])
            exps.append(expression[i])
            start_num_idx = i + 1
    numbers.append(expression[start_num_idx:])

    for exp_seq in permutations(list(set(exps))):
        new_exps = deepcopy(exps)
        new_nums = deepcopy(numbers)

        for exp in exp_seq:
            before_exp_used = False
            new_nums_tmp = []
            for i, num in enumerate(new_nums):
                if i == len(new_nums) - 1:
                    if not before_exp_used:
                        new_nums_tmp.append(num)
                    break
                if exp == new_exps[i]:
                    sub_result = str(eval(new_nums[i] + exp + new_nums[i + 1]))
                    new_nums[i+1] = sub_result
                    if before_exp_used:
                        new_nums_tmp[-1] = sub_result
                    else:
                        new_nums_tmp.append(sub_result)
                    before_exp_used = True
                else:
                    if not before_exp_used:
                        new_nums_tmp.append(num)
                    before_exp_used = False

            new_nums = new_nums_tmp.copy()
            new_exps = [e for e in new_exps if e != exp]

        sub_result = abs(int(new_nums[0]))
        ret = max(ret, sub_result)
    return ret

print(solution(testCases[0][0]))