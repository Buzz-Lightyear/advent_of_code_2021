def get_power_consumption():
    pos_one_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pos_zero_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open("input.txt", "r") as f:
        lines = [list(map(int, x.rstrip())) for x in f.readlines()]
        for line in lines:
            for i in range(12):
                if line[i] == 0:
                    pos_zero_count[i] += 1
                else:
                    pos_one_count[i] += 1

    gamma = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    epsilon = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

    for i in range(12):
        if pos_one_count[i] > pos_zero_count[i]:
            gamma[i] = '1'
        else:
            epsilon[i] = '1'
    
    return int(''.join(gamma), 2) * int(''.join(epsilon), 2)

def get_life_support():
    pos_one_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    pos_zero_count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    with open("input.txt", "r") as f:
        lines = [list(map(int, x.rstrip())) for x in f.readlines()]
        for line in lines:
            for i in range(12):
                if line[i] == 0:
                    pos_zero_count[i] += 1
                else:
                    pos_one_count[i] += 1

    gamma = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
    epsilon = ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']

    for i in range(12):
        if pos_one_count[i] > pos_zero_count[i]:
            gamma[i] = '1'
        else:
            epsilon[i] = '1'

    def get_most(values, i):
        one_list = [value for value in values if value[i] == 1]
        zero_list = [value for value in values if value[i] == 0]

        if len(one_list) >= len(zero_list):
            return one_list
        else:
            return zero_list
    
    def get_least(values, i):
        one_list = [value for value in values if value[i] == 1]
        zero_list = [value for value in values if value[i] == 0]

        if len(one_list) < len(zero_list):
            return one_list
        else:
            return zero_list

    oxygen_list = lines
    co2_list = lines
    for i in range(12):
        if len(oxygen_list) > 1:
            oxygen_list = get_most(oxygen_list, i)
        if len(co2_list) > 1:
            co2_list = get_least(co2_list, i)

    oxygen = int(''.join([str(x) for x in oxygen_list.pop()]), 2)
    co2 = int(''.join([str(x) for x in co2_list.pop()]), 2)

    return oxygen * co2



if __name__ == '__main__':
    print(get_life_support())