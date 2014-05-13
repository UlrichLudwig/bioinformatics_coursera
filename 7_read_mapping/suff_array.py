import operator
from common import small_example, read_dataset, big_example


def suf_array(text):
    indices = (i for i in range(len(text)))
    return sorted(indices, key=lambda i: text[i:])


#text, out = small_example()
#text = read_dataset()
#text, out = big_example()
text = open('test.txt').read()
print(', '.join(map(str, suf_array(text))))
