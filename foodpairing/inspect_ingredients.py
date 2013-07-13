#!/usr/bin/env python

import sys
import json
from collections import Counter

import cookpad_helper

def main():
    ingredients_counter = Counter()

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        for line in f:
            recipe = json.loads(line.strip())
            ingredients = recipe['ingredients']

            for ingredient in ingredients:
                normalized_ingredient = cookpad_helper.normalize(ingredient)
                ingredients_counter[normalized_ingredient] += 1

    for ingredient, count in ingredients_counter.most_common(1000):
        print('{}\t{}'.format(ingredient.encode('utf8'), count))


if __name__ == '__main__':
    main()
