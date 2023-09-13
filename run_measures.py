#!/usr/bin/env python
from share import years
import pandas as pd
import nxneo4j as nx
import pickle

def main():
    for year_label in years:
        # To open the network
        G = pickle.load(open(f'strong_G_{year_label}.pickle', 'rb'))
        measures = {}
        # Measures
        del response
        response = nx.pagerank(G)
        measures["sorted_pagerank"] = sorted(response.items(), key=lambda x: x[1], reverse=True)

        del response
        response = nx.betweenness_centrality(G)
        measures["sorted_bw"] = sorted(response.items(), key=lambda x: x[1], reverse=True)

        del response
        response = nx.closeness_centrality(G)
        measures["sorted_cc"] = sorted(response.items(), key=lambda x: x[1], reverse=True)

        del response
        communities = nx.label_propagation_communities(G)
        measures["sorted_communities"] = sorted(communities, key=lambda x: len(x), reverse=True)

        del response
        response = nx.clustering(G)
        measures["biggest_coefficient"] = sorted(response.items(), key=lambda x: x[1], reverse=True)

        pickle.dump(measures, open(f'/Users/almacuevas/work_projects/conferencias_matutinas_amlo/measures/measures_{year_label}.pickle', 'wb'))

if __name__ == "__main__":
    main()
    print("Done!")
