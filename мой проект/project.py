import json
import ndjson
import pandas as pd
import numpy as np
import seaborn as sns


with open('Новая папка/results/result.json', 'r', encoding='utf-8') as f:
    data = json.load(f)  # Читаем как массив

# Сохраняем как NDJSON (каждый объект на новой строке)
with open('Новая папка/results/result.ndjson', 'w', encoding='utf-8') as f:
    for item in data:
        json.dump(item, f, ensure_ascii=False)
        f.write('\n')  # Важно для NDJSON!


# reading reviews from json file
#with open('Новая папка/results/result.json', 'r', encoding='utf-8') as f:
#    data = ndjson.load(f)



reviews_df = pd.DataFrame(data)

reviews_df.head()

reviews_df.shape

reviews_df.info()

sns.countplot(data = reviews_df, x='rating')

len(reviews_df['product_id'].value_counts(dropna=False))

#Undersampling of Reviews

one_500 = reviews_df[reviews_df['rating'] == 1].sample(n=500)
two_500 = reviews_df[reviews_df['rating'] == 2].sample(n=100)
three_500 = reviews_df[reviews_df['rating'] == 3].sample(n=100)
four_500 = reviews_df[reviews_df['rating'] == 4].sample(n=100)
five_500 = reviews_df[reviews_df['rating'] == 5].sample(n=100)

undersampled_reviews = pd.concat([one_500, two_500, three_500, four_500, five_500], axis=0)

undersampled_reviews['rating'].value_counts(dropna=False)

sns.countplot(data=undersampled_reviews, x='rating')

# Random Sampling of 100K Reviews

sample_100K_revs = reviews_df.sample(n=600, random_state=42)
undersampled_reviews.to_csv("data/small_corpus.csv")
sample_100K_revs.to_csv("data/big_corpus.csv")