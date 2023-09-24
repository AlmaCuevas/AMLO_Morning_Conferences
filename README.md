# TODO:
* The world_data_lemma_set can be convert into Graphs but only one at a time can be run, otherwise they all fail because of memory shortage.
* From the measures, BC takes so long, I have never finish one. No idea if it'll even work.

# Notes: 
* No singularization was done bc it run horribly.
  * The "Gracias" was being changed to "Gracia"
* The graph doesn't represent the frequency to which the words appear, the bag of words is a set. The graph is just meant to represent how the nouns relate to other nouns.
* The creation of the graph doesn't take long, the drawing does. That's why there are files to run everything, instead of ipynb.
  * Drawings are not useful. There are too many dots to visualize.
  * The drawing seems impossible so far in Gephi or Neo4j. The graphs are too big and no computer available can load it.
  * The nodes doesn't have sense if the results are verbs. That's why the folder "spacy_graph_metainfo" only have a set of nouns and adjectives.

# Other ideas
* A different project should be done to quantize the most frequent nouns (that's the idea on "most_frequent_words.ipynb)
* A different project can be "predict which year it is" by the entries. Could be done with BERT. But it sounds silly.
