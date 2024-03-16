#!/usr/bin/env python
from share import years
import pandas as pd
import spacy

def main():
    nlp = spacy.load('es_core_news_lg')

    for year_label in years:
        print(year_label)
        data = pd.read_csv(f'most_frequent/df_{year_label}.csv')

        # Using spaCy to parse
        tokens = []
        lemma = []
        pos = []
        parsed_doc = []

        for doc in nlp.pipe(data['term'].astype('unicode').values, batch_size=50):
            if doc.has_annotation("DEP"):
                parsed_doc.append(doc)
                tokens.append(''.join([n.text for n in doc]))
                lemma.append(''.join([n.lemma_ for n in doc]))
                pos.append(''.join([n.pos_ for n in doc]))
            else:
                # We want to make sure that the lists of parsed results have the
                # same number of entries of the original Dataframe, so add some blanks in case the parse fails
                tokens.append(None)
                lemma.append(None)
                pos.append(None)

        data['parsed_doc'] = parsed_doc
        data['comment_tokens'] = tokens
        data['comment_lemma'] = lemma
        data['pos_pos'] = pos
        # %% md
        ## Basic checks of the parsed data
        # %%
        world_data = data.loc[data['pos_pos'].isin(['NOUN', 'ADJ'])].reset_index(drop=True)
        # %%
        data = world_data

        tokens = []
        lemma = []
        pos = []
        parsed_doc = []

        for doc in nlp.pipe(data["comment_lemma"].astype('unicode').values, batch_size=50):
            if doc.has_annotation("DEP"):
                parsed_doc.append(doc)
                tokens.append(''.join([n.text for n in doc]))
                lemma.append(''.join([n.lemma_ for n in doc]))
                pos.append(''.join([n.pos_ for n in doc]))
            else:
                # We want to make sure that the lists of parsed results have the
                # same number of entries of the original Dataframe, so add some blanks in case the parse fails
                parsed_doc.append(None)
                tokens.append(None)
                lemma.append(None)
                pos.append(None)

        data['parsed_doc'] = parsed_doc
        data['comment_tokens'] = tokens
        data['comment_lemma'] = lemma
        data['pos_pos'] = pos

        world_data=data
        world_data.to_csv(
            f'/conferencias_matutinas_amlo/spacy_graph_metainfo/world_data_lemma_set_{year_label}.csv')

if __name__ == "__main__":
    main()
    print("Done!")
