params = list(map(int, input().split()))[:3]
n, start_ind, end_ind = params[0], params[1], params[2] 

numbers = list(map(int, input().split()))[:n]

reversed_list = list(reversed(numbers[start_ind - 1: end_ind]))

numbers[start_ind - 1: end_ind] = reversed_list

print(*numbers)

