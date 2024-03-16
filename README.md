# Processing of the Morning Conferences: "Las mañaneras"

Database obtained from: https://github.com/NOSTRODATA/conferencias_matutinas_amlo @nostrodata https://www.nostrodata.com

The code from the Notebooks are the didactic version. The .py are meant to be run in the terminal.

Descriptions:
* Notebook "0. basic_extractions" runs the tree of .csv files and joins them in one. Plus, it contains two basic graphs.
* Notebook "1. most_frequent_words" has the TfidfVectorizer
* Notebook "2. networkx_and_measures" was an edition from https://www.kaggle.com/code/caractacus/thematic-text-analysis-using-spacy-networkx
* Notebook "3. measures_summary" is to visualize the measures from above
* Notebook "4. unsupervised_topics_classification_complete_yearconferences" for more information check: https://elmundodelosdatos.com/topic-modeling-gensim-asignacion-topicos/

## Abstract
The "Mañaneras" are conferences that the president of Mexico holds each weekday to answer various questions, explain policies, give directions, and impart historical lessons. This article analyzes the dialogues in the Morning Conference transcripts, in which the most relevant themes and their evolution over time are examined. Through this analysis, we seek to understand the trending topics in the interactions between Andrés Manuel López Obrador, President of Mexico, and the participants, primarily representatives of the Mexican press, spanning from December 7, 2018, to July 10. 2023. This study offers a detailed view of current and changing concerns in the country, as well as how these conversations influence political dynamics and decision-making in Mexico.

### Word count for each year.
Each participant can intervene; each intervention has a word count averaged per conference. Thus, per year, we can see how long each intervention lasts. In other words, how long a comment turn lasts.

<img width="544" alt="word_count" src="https://github.com/AlmaCuevas/AMLO_Morning_Conferences/assets/46833474/1e19f778-8ba6-4659-8c2a-eb46063aa52e">

Word count for each year. The first (2018) and last (2023) years don’t
represent the whole year.

### Number of total participations per participant per year.
After grouping the main characters into three groups, they counted how many times that group appeared. In this way we can know if there is a balance between actors or if one of the groups is the protagonist of the conferences.

<img width="570" alt="participations" src="https://github.com/AlmaCuevas/AMLO_Morning_Conferences/assets/46833474/f8f81459-3f4c-4496-9564-0df8ef1b2299">

### Unique words across the Top 50 most repeated terms per year.
Only one ngram was chosen, that is, only one word. We then classified these words according to their Part-of-Speech tag using Spacy's 'es_core_news_lg' model, a linguistic model in Spanish that is based on written text (such as news and media). We only kept the words that belong to the 'NOUN' group. We consider words like "good morning" or "inaudible" as noise; they are part of the conversation but do not contain any relevant information.
The reason for using only the top 50 is that as more words are added, by eliminating repetitions based on lemmatization, relevant topics that are repeated per year begin to be eliminated. The results are the origin term, not its lemma.

The text has been translated from Spanish to English. Most of the words had only one ngram, but due to translation, there were two exceptions. The word 'fiscalía' translates to 'prosecutor's office', and 'Luna' refers to García Luna, not the moon. Although lemmatization was used, the translation of the words led to the appearance of 'doctors', which corresponds to the Spanish word 'médicos', and 'doctor', which comes from the Spanish 'doctor'.

<img width="636" alt="freq_years" src="https://github.com/AlmaCuevas/AMLO_Morning_Conferences/assets/46833474/bb3cdc80-40b9-4410-80ee-808d96a313cb">
