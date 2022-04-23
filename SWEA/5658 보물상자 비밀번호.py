T = int(input())

def find_biggest_number(numbers, N, K):
    length = int(N/4)
    n_list = []
    hex_list = []
    for _ in range(length):
        for i in range(0, N, length):
            str_n = numbers[i:i+length]
            n = int(str_n, 16)
            if n not in n_list:
                hex_list.append(str_n)
                n_list.append(n)
        new_numbers = numbers[1:N] + numbers[0]
        numbers = new_numbers

    n_list = sorted(n_list, reverse=True)

    return n_list[K-1]



for i in range(T):
    N, K = map(int, input().split())
    numbers = input()
    print("#%d %d"%(i+1,find_biggest_number(numbers, N, K)))

