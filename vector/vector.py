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

class Document:
    document_count = 0

    def __init__(self, name):
        self.name = name
        self.keywords = {}
        self.tf = {}
        self.sim = {}
        Document.document_count += 1

TF_K = 0.5

keywords = []
for keyword in input("Keyword (seperate by space): ").split():
    keywords.append(Keyword(keyword))
# keywords = input("Keyword (seperate by space): ").split()

documents = []
while (True):
    name = input("Document name/number: ")
    document = Document(name)

    # ask for each keyword count
    for keyword in keywords:
        document.keywords[keyword] = int(input("[" + name + "] Keyword '" + keyword.name + "' count: "))
        keyword.count += 1

    # add document to list
    documents.append(document)

    prompt = input('Do you want to add more documents? (y/n): ')
    if (prompt not in ['', 'y', 'yes']):
        break

# find idf
for keyword in keywords:
    keyword.idf = idf(Keyword.keyword_count, keyword.count)

# find tf & sim
for document in documents:
    # find maximum frequencies in documents
    max_freq = document.keywords[max(document.keywords, key=document.keywords.get)]

    # find tf & sim
    for keyword, freq in document.keywords.items():
        document.tf[keyword] = tf(freq, max_freq, TF_K)
        document.sim[keyword] = document.tf[keyword] * keyword.idf

for document in documents:
    print(vars(document))