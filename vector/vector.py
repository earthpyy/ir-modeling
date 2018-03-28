from abc import ABC
from tf_idf import tf, idf

class Keyword:
    keyword_count = 0

    def __init__(self, name):
        self.name = name
        self.count = 0
        self.idf = None
        Keyword.keyword_count += 1

    def __repr__(self):
        return self.name

class WeightableObject(ABC):
    def __init__(self, name):
        self.name = name
        self.keywords = {}
        self.tf = {}
        self.weight = {}
    
    def __repr__(self):
        return self.name

class Document(WeightableObject):
    document_count = 0

    def __init__(self, name):
        super().__init__(name)
        Document.document_count += 1

class Query(WeightableObject):
    def __init__(self, name):
        super().__init__(name)
        self.deg = {}

TF_K = 0.5

def sum_pow(document):
    result = 0;
    for weight in document.weight.values():
        result += pow(weight, 2)
    return result

keywords = []
for keyword in input("Keyword (seperate by space): ").split():
    keywords.append(Keyword(keyword))
# keywords = input("Keyword (seperate by space): ").split()

documents = []
while (True):
    document = Document(input("Document name/number: "))

    # ask for each keyword count
    for keyword in keywords:
        document.keywords[keyword] = int(input("[" + document.name + "] Keyword '" + keyword.name + "' count: "))
        keyword.count += 1

    # add document to list
    documents.append(document)

    prompt = input('Do you want to add more documents? (y/n): ')
    if (prompt not in ['', 'y', 'yes']):
        break

# find idf
for keyword in keywords:
    keyword.idf = idf(Keyword.keyword_count, keyword.count)

for document in documents:
    # find maximum frequencies in documents
    max_freq = document.keywords[max(document.keywords, key=document.keywords.get)]

    # find tf & weight
    for keyword, freq in document.keywords.items():
        document.tf[keyword] = tf(freq, max_freq, TF_K)
        document.weight[keyword] = document.tf[keyword] * keyword.idf

queries = []
while (True):
    query = Query(input("Query name/number: "))

    # ask for each keyword count in query
    for keyword in keywords:
        query.keywords[keyword] = int(input("[" + query.name + "] Keyword '" + keyword.name + "' count: "))

    # add query to list
        queries.append(query)

    prompt = input('Do you want to add more documents? (y/n): ')
    if (prompt not in ['', 'y', 'yes']):
        break

for query in queries:
    max_freq = query.keywords[max(query.keywords, key=query.keywords.get)]

    # find tf & weight
    for keyword, freq in query.keywords.items():
        query.tf[keyword] = tf(freq, max_freq, TF_K)
        query.weight[keyword] = query.tf[keyword] * keyword.idf

    # find degree of similarity
    for document in documents:
        query.deg[document] = 0;
        for keyword, weight in document.weight.items():
            query.deg[document] += weight * query.weight[keyword]
        query.deg[document] /= (sum_pow(query) * sum_pow(document))

for document in documents:
    print(vars(document))

for query in queries:
    print(vars(query))