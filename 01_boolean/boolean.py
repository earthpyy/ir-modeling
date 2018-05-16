import sys, os, csv

keywords = []
documents = {}

with open(os.path.join(sys.path[0], 'sample.csv'), 'r') as fp:
    reader = csv.reader(fp, delimiter=',')
    for keyword in next(reader)[1:]:
        keywords.append(keyword)
    for row in reader:
        documents[row[0]] = []
        for val in row[1:]:
            documents[row[0]].append(val)