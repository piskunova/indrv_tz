from google_trans_new import google_translator
import pandas as pd
from sklearn.utils import shuffle
import tqdm
import time

translator = google_translator()
data_file = '../data/twi_data.tsv'


def translate(tweet, lang='en'):
    time.sleep(1)
    return translator.translate(tweet, lang_tgt=lang)


df = shuffle(pd.read_csv(data_file, sep='\t')).reset_index(drop=True)[:500]
with open('../data/twi_data_translated.tsv', 'w') as f:
    f.write('date\tuser_id\tcity\ttweet\ttranslated_tweet\n')
    for _, row in tqdm.tqdm(df.iterrows(), total=500):
        f.write(f'{row.date}\t{row.user_id}\t{row.city}\t{row.tweet}\t{translate(row.tweet)}\n')
