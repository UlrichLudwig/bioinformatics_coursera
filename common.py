import os
path = os.path.dirname(os.path.realpath(__file__))


def big_example(fname='example.txt'):
    with open(os.path.join(path, fname)) as f:
        input = []
        output = []
        reading_input = True
        for line in f.readlines():
            line = line.strip()
            if line == 'Input' or line == 'Input:' or line == 'Sample Input:' or line == '':
                continue
            if line == 'Output' or line == 'Output:' or line == 'Sample Output:':
                reading_input = False
                continue
            if reading_input:
                input.append(line)
            else:
                output.append(line)

        open('example_result.txt', 'w').write('\n'.join(output))

        if len(input) == 1:
            input = input[0]
        if len(output) == 1:
            output = output[0]
        return input, output


def small_example(fname='small_example.txt'):
    return big_example(fname)


def read_dataset(fname='dataset.txt'):
    data = open(os.path.join(path, fname)).read().split('\n')
    data = list(filter(None, data))
    if len(data) == 1:
        data = data[0]
    return data


def write_result(result, fname='result.txt'):
    print()
    print(result)
    result = result.upper()
    open(os.path.join(path, fname), 'w').write(result)
