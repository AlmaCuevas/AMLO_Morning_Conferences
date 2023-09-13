# TODO:
* The result from the measures have to be recorded in txt files, first analyze one and decide whether the information is useful and how it can be interpreted.
* Memory usage failed when executing 2019 graph creation. The world_data_lemma_set is available, but you have to continue from there.

# Notes: 
* No singularization was done bc it run horribly.
  * The "Gracias" was being changed to "Gracia"
* The graph doesn't represent the frequency to which the words appear, the bag of words is a set. The graph is just meant to represent how the nouns relate to other nouns.
* The creation of the graph doesn't take long, the drawing does. That's why there are files to run everything, instead of ipynb.
  * Drawings are not useful. There are too many dots to visualize.
  * For the drawing use Gephi, as teacher suggests.
  * The nodes doesn't have sense if the results are verbs. That's why the spacy_graph_metainfo only have a set of nouns and adjectives.

# Other ideas
* A different project should be done to quantize the most frequent nouns (that's the idea on "most_frequent_words.ipynb)
* A different project can be predict which year it is by the entries. Could be done with BERT. But it sounds silly.
