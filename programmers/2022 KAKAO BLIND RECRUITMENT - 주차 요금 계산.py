from collections import defaultdict

def time_diff(t_in, t_out):
    in_h, in_m = int(t_in.split(':')[0]), int(t_in.split(':')[1])
    out_h, out_m = int(t_out.split(':')[0]), int(t_out.split(':')[1])
    return (out_h * 60 + out_m) - (in_h * 60 + in_m)


def solution(fees, records):
    answer = []
    base_time, base_fee, time_unit, fee_unit = fees
    car_nums = []
    car_info = defaultdict(list)
    for record in records:
        t, car, status = record.split(' ')
        car_info[car].append((t, status))
        if car not in car_nums: car_nums.append(car)

    for car_num in sorted(car_nums):
        in_flag = False
        in_time = ''
        t_diffs = []
        print(car_num)
        for t, status in car_info[car_num]:
            if status == 'IN':
                in_time = t
                in_flag = True
            else:
                t_diffs.append(time_diff(in_time, t))
                in_flag = False
        if in_flag:
            t_diffs.append(time_diff(in_time, '23:59'))

        print(t_diffs, sum(t_diffs))
        total_time = sum(t_diffs)
        fee = base_fee
        if total_time - base_time > 0:
            fee += ((total_time - base_time) // time_unit) * fee_unit
            if (total_time - base_time) % time_unit != 0:
                fee += fee_unit

        answer.append(fee)


    return answer


solution(
    [180, 5000, 10, 600],
    ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
     "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
)
