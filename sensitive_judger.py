import pandas as pd
import re
from collections import Counter


sensitive_words = pd.read_csv('data/sensitive_words_lib.csv').name_word.to_list()

df_products = pd.read_csv('data/special_products_list.csv')
df = df_products[df_products.special_positive_rate_by_parcel > 10]

idx = 30000
print(df.iloc[idx])
prod_id = df.iloc[idx]['product_id'].lower()
prod_name = df.iloc[idx]['product_name'].lower()
prod_tags = df.iloc[idx]['tags'].split(',')

elem = re.sub('\?|/|,|!|&|\.|\$|\(|\)|pcs|-|\+', ' ', prod_name)
elem = re.sub('\\s+', ' ', elem)
name_words = elem.split(' ')

name_words_sensitive = 0
for word in name_words:
    if word in sensitive_words:
        name_words_sensitive += 1

tags_sensitive = 0
for tag in prod_tags:
    if tag in sensitive_words:
        tags_sensitive += 1


print('product_id = {}'.format(prod_id))
print('Total words in name = {}, in which sensitive words number = {}'.format(len(name_words), name_words_sensitive))
print('Total words in tags = {}, in which sensitive words number = {}'.format(len(prod_tags), tags_sensitive))