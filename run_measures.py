#!/usr/bin/env python
from share import years
import pandas as pd
import pickle
import networkx as nx
import sys

def main(year_label: str):
        #for year_label in ["2019"]:
        # To open the network
        G = pickle.load(open(f'/Users/almacuevas/work_projects/conferencias_matutinas_amlo/graphs/strong_G_{year_label}.pickle', 'rb'))
        measures = {}
        # Measures
        print("Start Page Rank")
        response = nx.pagerank(G)
        measures["sorted_pagerank"] = sorted(response.items(), key=lambda x: x[1], reverse=True)
        pickle.dump(measures, open(f'/Users/almacuevas/work_projects/conferencias_matutinas_amlo/measures/measures_{year_label}.pickle', 'wb'))

        print("Start BC")
        del response
        response = nx.betweenness_centrality(G)
        measures["sorted_bw"] = sorted(response.items(), key=lambda x: x[1], reverse=True)

        pickle.dump(measures, open(f'/Users/almacuevas/work_projects/conferencias_matutinas_amlo/measures/measures_{year_label}.pickle', 'wb'))
        print("Start CC")
        del response
        response = nx.closeness_centrality(G)
        measures["sorted_cc"] = sorted(response.items(), key=lambda x: x[1], reverse=True)

        pickle.dump(measures, open(f'/Users/almacuevas/work_projects/conferencias_matutinas_amlo/measures/measures_{year_label}.pickle', 'wb'))
        print("Start Clustering")
        del response
        response = nx.clustering(G)
        measures["biggest_coefficient"] = sorted(response.items(), key=lambda x: x[1], reverse=True)

        pickle.dump(measures, open(f'/Users/almacuevas/work_projects/conferencias_matutinas_amlo/measures/measures_{year_label}.pickle', 'wb'))

if __name__ == "__main__":
        main(sys.argv[1])
        print("Done!")
