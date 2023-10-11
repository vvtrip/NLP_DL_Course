import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
nltk.download('stopwords')

def Tokenize(string):
  str_lst = string.split()
  return str_lst

def RemoveStopWords(string):
  str_lst = string
  stop_words = stopwords.words('english')
  print(str_lst)
  for word in str_lst:
    print(word)
    if word.lower() in stop_words:
      str_lst.remove(word)

  return str_lst

def Lemmatize(string):
  str_lst = string
  lem = WordNetLemmatizer()
  lem_lst=[]

  for word in str_lst:
    lem_lst.append(lem.lemmatize(word))

  return lem_lst, str_lst

def Refine():
  string = input()
  string = Tokenize(string)
  string = RemoveStopWords(string)
  string, words = Lemmatize(string)
  string = " ".join(string)
  print(f"refined string: {string}")

Refine()