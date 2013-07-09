#!/usr/bin/env python

import sys
import argparse
import itertools
from collections import defaultdict

import networkx as nx


def load_data(filename):
    ingredient2compounds = defaultdict(set)
    compound2ingredients = defaultdict(set)

    with open(filename, 'r') as f:
        for line in f:
            columns = line.strip().split('\t')
            if not len(columns) == 6:
                print line
                sys.exit(1)
            compound = columns[-2]
            ingredients = map(lambda i: i.strip(), columns[-1].split(','))

            for ingredient in ingredients:
                ingredient2compounds[ingredient].add(compound)
                compound2ingredients[compound].add(ingredient)
    return ingredient2compounds, compound2ingredients


def generate_graph(ingredient2compounds, compound2ingredients):
    graph = nx.Graph()

    # TODO: don't consider all possible pairs
    ingredients = ingredient2compounds.iterkeys()
    for ingredient1, ingredient2 in itertools.combinations(ingredients, 2):
        weight = len(ingredient2compounds[ingredient1] &
                     ingredient2compounds[ingredient2])
        if weight == 0:
            continue

        graph.add_edge(ingredient1, ingredient2, weight=weight)
        graph.node[ingredient1]['prevalence'] = len(ingredient2compounds[ingredient1])
        graph.node[ingredient2]['prevalence'] = len(ingredient2compounds[ingredient2])

    return graph

def main():
    if len(sys.argv) != 3:
        sys.stderr.write('Usage: %s /path/to/flavornet.txt output.gml\n'.format(sys.argv[0]))
        sys.exit(1)

    ingredient2compounds, compound2ingredients = load_data(sys.argv[1])
    graph = generate_graph(ingredient2compounds, compound2ingredients)

    with open(sys.argv[2], 'w') as f:
        for line in nx.generate_gml(graph):
            f.write('{}\n'.format(line))

if __name__ == '__main__':
    main()
