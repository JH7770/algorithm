def solution(operations):
    answer = []

    for command in operations:
        oper, num = command.split(" ")
        num = int(num)

        if oper == "I":
            answer.append(num)
        elif oper == "D" and num == 1 and answer:
            answer.remove(max(answer))
        elif oper == "D" and num == -1 and answer:
            answer.remove(min(answer))


    if not answer:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    return answer

print(solution(["I 7","I 5","I -5","D -1"]))