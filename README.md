# TODO:

* The transcript doesn't have all the spaces between a two words when a dot is in the middle.
  * Example: "arriba.Entonces"
  * Solution: You have to separate by ,.? etc
* The creation of the graph doesn't take long, the drawing does. Move the ipynb to a runable python file to run everything
out of Pycharm (in the terminal).
  * Drawings are not useful. There are too many dots to visualize.
* The result from the measures have to be recorded in txt files, firt analyze one and decide whether the information is useful and how it can be interpreted.
* The nodes doesn't have sense if the results are verbs. Pre-process to only have nouns.


# Notes: 
* No singularization was done bc it run horribly.
  * The "Gracias" was being changed to "Gracia"
* The graph doesn't represent the frequency to which the words appear, the bag of words is a set. The graph is just meant to represent how the nouns relate to other nouns.
* A different project should be done to quantize the most frequent nouns (that's the idea on "most_frequent_words.ipynb)
* A different project can be predict which year it is by the entries. Could be done with BERT. But it sounds silly.
