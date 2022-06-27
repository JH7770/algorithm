from collections import defaultdict

def init():
    i = 1
    num2loc = defaultdict(tuple)
    loc2num = defaultdict(int)
    for r in range(3):
        for c in range(3):
            num2loc[i] = (r, c)
            loc2num[(r, c)] = i
            i += 1

    num2loc[0] = (3, 1)
    loc2num[(3, 1)] = 0
    return num2loc, loc2num

def get_dist(loc1, loc2):
    r1, c1 = loc1
    r2, c2 = loc2
    return abs(r1 - r2) + abs(c1 - c2)



def solution(numbers, hand):
    answer = ''
    num2loc, loc2num = init()
    lefthand = (3, 0) # default '*'
    righthand = (3, 2) # default '#'

    for n in numbers:
        print(loc2num[lefthand], loc2num[righthand])
        if n in [1, 4, 7]: # only left hand
            answer += 'L'
            lefthand = num2loc[n]
        elif n in [3, 6, 9]: # only right hand
            answer += 'R'
            righthand = num2loc[n]
        else: # both
            lefthand_dist = get_dist(lefthand, num2loc[n])
            righthand_dist = get_dist(righthand, num2loc[n])
            print(num2loc[n], lefthand, lefthand_dist, righthand, righthand_dist)
            if (lefthand_dist < righthand_dist) or (lefthand_dist == righthand_dist and hand == "left"):
                answer += 'L'
                lefthand = num2loc[n]
            elif (lefthand_dist > righthand_dist) or (lefthand_dist == righthand_dist and hand == "right"):
                answer += 'R'
                righthand = num2loc[n]
    print(answer)
    return answer



solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], 'right')