import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize

def MakeCorpus(*args):
  corp = set()
  for sent in args:
    for tok in word_tokenize(sent):
      corp.add(tok)
  return list(corp)