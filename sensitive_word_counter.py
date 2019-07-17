import pandas as pd
import re
from collections import Counter

df = pd.read_csv('data/top_products_sensitive.csv')
df = df[df.sold_in_distinct_parcels > 5]
freq_threshold = 30

tags_list = df.tags.to_list()

words = []
for elem in tags_list:
    words += elem.split(',')

c = Counter(words)

with open('tag_result.csv', 'w+', encoding='utf-8', newline='') as f:
    f.write('tag,frequency\n')
    while len(c) > 0:
        e = c.popitem()
        f.write(e[0] + ',' + str(e[1]) + '\n')


prod_name_list = df.product_name.str.lower().to_list()

name_words = []
for elem in prod_name_list:
    elem = re.sub('\?|/|,|!|&|\.|\$|\(|\)|pcs|-|\+', ' ', elem)
    elem = re.sub('\\s+', ' ', elem)
    name_words += elem.split(' ')

c1 = Counter(name_words)

with open('prod_name_result.csv', 'w+', encoding='utf-8', newline='') as f:
    f.write('name_word,frequency\n')
    d = dict()
    while len(c1) > 0:
        e = c1.popitem()
        if e[1] >= freq_threshold and len(e[0]) > 2:
            d[e[0]] = e[1]
    d1 = sorted(d.items(), key=lambda kv: (kv[1], kv[0]))
    while len(d1) > 0:
        e = d1.pop()
        if e[0] != '':
            try:
                int(e[0])
            except ValueError:
                f.write(e[0] + ',' + str(e[1]) + '\n')
