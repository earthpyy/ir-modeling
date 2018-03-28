import math

def tf(freq, max, k=0.5):
    return k + (k * freq / max)

def idf(n, freq):
    return math.log10(1 + (n / freq))

if __name__ == '__main__':
    docN = int(input('[IDF] docN: '))

    while (True):
        freq = int(input('[TF] freq: '))
        max = int(input('[TF] max: '))
        # docN = int(input('docN: '))
        docFreq = int(input('[IDF] freq: '))

        tf_val = tf(freq, max)
        idf_val = idf(docN, docFreq)
        print('TF:', tf_val)
        print('IDF:', idf_val)
        print('TF*IDF:', tf_val * idf_val)
        print()