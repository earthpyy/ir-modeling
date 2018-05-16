import sys, os, csv

keywords = []
documents = []

with open(os.path.join(sys.path[0], 'sample.csv'), 'r') as fp:
    reader = csv.reader(fp, delimiter=',')
    n = len(next(reader)) - 1
    for i in range(pow(2, n)):
        keywords.append([])

    for row in reader:
        documents.append(row[0])
        bin_str = ''.join(row[1:])
        keywords[int(bin_str, 2)].append(len(documents) - 1)