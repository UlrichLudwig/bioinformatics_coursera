def composition(k, genome):
    return sorted((genome[i:i + k] for i in range(len(genome) - k + 1)))


if __name__ == '__main__':
    with open('dataset.txt') as f:
        text = f.read()

    result = composition(
        int(text.split()[0]),
        text.split()[1])

    with open('result.txt', 'w') as r:
        print('\n'.join(result), file=r)