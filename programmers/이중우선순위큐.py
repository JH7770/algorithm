def solution(operations):
    answer = []

    for command in operations:
        # 명령어를 공백을 기준으로 분리 ex) "D -1" -> "D", "-1"
        oper, num = command.split(" ")
        num = int(num) # string -> integer 변환

        if oper == "I": # Insert 명령인 경우 리스트에 추가
            answer.append(num)
        elif oper == "D" and num == 1 and answer: # D 1 명령어인 경우 리스트의 최대값 삭제
            answer.remove(max(answer))
        elif oper == "D" and num == -1 and answer: # D -1 명령어인 경우 리스트의 최솟값 삭제
            answer.remove(min(answer))

    if not answer: # 리스트에 아무 값이 없는 경우 answer = [0, 0]
        answer = [0, 0]
    else: # 리스트에 값이 있는 경우 answer = [최대값, 최솟값]
        answer = [max(answer), min(answer)]
    return answer

print(solution(["I 7","I 5","I -5","D -1"]))