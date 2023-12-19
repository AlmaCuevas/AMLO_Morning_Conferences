#!/usr/bin/env python
import pandas as pd
import networkx as nx
import pickle
import spacy
import sys

def main(year_label: str):

    nlp = spacy.load('es_core_news_lg')
    world_data = pd.read_csv(
        f'/conferencias_matutinas_amlo/spacy_graph_metainfo/world_data_lemma_set_{year_label}.csv')

    data = pd.DataFrame({"term": list(set(world_data['comment_lemma']))})
    print("Start parsing with Spacy")
    # Using spaCy to parse
    parsed_doc = []

    for doc in nlp.pipe(data['term'].astype('unicode').values, batch_size=50):
        if doc.has_annotation("DEP"):
            parsed_doc.append(doc)
    # takes 1s for 500 nodes - but of course this won't scale linearly!
    raw_G = nx.Graph()  # undirected
    n = 0

    data['parsed_doc'] = parsed_doc
    print("Similarity calculation")
    for i in data['parsed_doc']:  # sure, it's inefficient, but it will do
        for j in data['parsed_doc']:
            if i != j:
                if not (raw_G.has_edge(j, i)):
                    sim = i.similarity(j)
                    raw_G.add_edge(i, j, weight=sim)
                    n = n + 1

    print(raw_G.number_of_nodes(), "nodes, and", raw_G.number_of_edges(), "edges created.")

    edges_to_kill = []
    min_wt = 0.4  # this is our cutoff value for a minimum edge-weight

    for n, nbrs in raw_G.adj.items():
        # print("\nProcessing origin-node:", n, "... ")
        for nbr, eattr in nbrs.items():
            # remove edges below a certain weight
            data = eattr['weight']
            if data < min_wt:
                # print('(%.3f)' % (data))
                # print('(%d, %d, %.3f)' % (n, nbr, data))
                # print("\nNode: ", n, "\n <-", data, "-> ", "\nNeighbour: ", nbr)
                edges_to_kill.append((n, nbr))

    print("\n", len(edges_to_kill) / 2, "edges to kill (of", raw_G.number_of_edges(), "), before de-duplicating")

    for u, v in edges_to_kill:
        if raw_G.has_edge(u, v):  # catches (e.g.) those edges where we've removed them using reverse ... (v, u)
            raw_G.remove_edge(u, v)

    pickle.dump(raw_G, open(f'/conferencias_matutinas_amlo/graphs/raw_G_{year_label}.pickle', 'wb'))


    strong_G = raw_G
    strong_G.remove_nodes_from(list(nx.isolates(strong_G)))

    pickle.dump(strong_G, open(f'/conferencias_matutinas_amlo/graphs/strong_G_{year_label}.pickle', 'wb'))

if __name__ == "__main__":
    main(sys.argv[1])
    print("Done!")
