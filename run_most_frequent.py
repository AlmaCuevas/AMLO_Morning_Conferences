#!/usr/bin/env python
from share import select_secondary_keywords_ngrams
from share import years
import pandas as pd

def main():
    all_df = pd.read_csv('all_df_preprocess.csv')
    for year_label in years:
        df_year = all_df.loc[all_df["Anio"] == int(year_label)]
        frequent_words = pd.DataFrame()
        frequent_words = select_secondary_keywords_ngrams(df_year.preprocess, 1, 1)  # [0:max_n]
        frequent_words.to_csv(f'/Users/almacuevas/work_projects/conferencias_matutinas_amlo/most_frequent/df_{year_label}.csv')

if __name__ == "__main__":
    main()
    print("Done!")