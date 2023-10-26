import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

def MakeCorpus(*args):
  corp = set()    
  for sent in args:
    for tok in word_tokenize(sent):
      corp.add(tok)
  return list(corp)

def PresenceAbsenceVectorization(*args):
  corp = MakeCorpus(*args)
  
  vecs = []
  print(corp)
  for sent in args:
    vec = [0]*len(corp)
    for tok in word_tokenize(sent):
      if tok in corp:
        vec[corp.index(tok)] = 1
    vecs.append(vec)    
  return vecs

def CountVectorization(*args):
  corpus = []

  for sent in args:
    corpus.append(sent)

  vectorizer = CountVectorizer()
  X = vectorizer.fit_transform(corpus)

  return  X.toarray()

def TFIDFVectorization(*args):
  corpus = []

  for sent in args:
    corpus.append(sent)

  vectorizer = TfidfVectorizer()
  X = vectorizer.fit_transform(corpus)

  return  X.toarray()