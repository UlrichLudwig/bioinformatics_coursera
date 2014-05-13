from common import small_example, big_example, read_dataset, write_result


def change(money, coins):
    min_change = [[] for _ in range(max(coins))]
    min_nums = [0] * max(coins)
    for sum in range(min(coins), money + 1):
        min_sum, min_c = min((min_nums[(sum - c) % max(coins)], c) for c in coins if c <= sum)
        min_nums[sum % max(coins)] = min_sum + 1
        min_change[sum % max(coins)] = min_change[(sum - min_c) % max(coins)] + [min_c]

    print(min_nums)
    print(min_change)
    return min_nums[money % sum], min_change[money % sum]

if __name__ == '__main__':
    input, output = small_example()
    input = read_dataset()
    print(change(int(input[0]), list(map(int, input[1].split(',')))))

