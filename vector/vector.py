from tf_idf import tf, idf

# class Keyword:
#     keyword_count = 0

#     def __init__(self, name):
#         self.name = name
#         Keyword.keyword_count += 1

class Document:
    document_count = 0

    def __init__(self, name):
        self.name = name
        self.keywords = {}
        self.tf = {}
        self.idf = {}
        Document.document_count += 1

# keywords = []
# for keyword in input("Keyword (seperate by space): ").split():
#     keywords.append(Keyword(keyword))
keywords = input("Keyword (seperate by space): ").split()

documents = []
while (True):
    name = input("Document name/number: ")
    document = Document(name)

    for keyword in keywords:
        document.keywords[keyword] = int(input("[" + name + "] Keyword '" + keyword + "' count: "))
    
    documents.append(document)

    prompt = input('Do you want to add more documents? (y/n): ')
    if (prompt not in ['', 'y', 'yes']):
        break

# for document in documents:
#     print(vars(document))