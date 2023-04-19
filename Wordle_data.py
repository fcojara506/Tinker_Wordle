import pandas as pd


# count the number of letter in each word
def clean_data(df,min_len = 5):
    df.word = df.word.str.strip()
    df.word = df.word.str.lower()
    df.word = df.word.str.replace('[0-9\,\.!?\-\/]','')
    df['count'] = df.word.str.len()
    df = df[df['count'] == min_len]
    df = df.reset_index(drop=True)
    return df

def read_data(csv_path = 'english_dictionary2.csv'):
    #read dictionary words
    en_dict = pd.read_csv(csv_path,names = ['word','freq'], header = 0)
    # filter only word with more than 5 letters
    en_long = list(clean_data(en_dict)['word'])
    en      = list(clean_data(en_dict).head(1000)['word'])
    return en, en_long