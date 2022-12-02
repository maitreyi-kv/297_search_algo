import re
import string
import Stemmer

STOPWORDS = set(['the', 'be', 'to', 'of', 'and', 'a', 'in', 'that', 'have',
                 'i', 'it', 'for', 'not', 'on', 'with', 'he', 'as', 'you',
                 'do', 'at', 'this', 'but', 'his', 'by', 'from', 'wikipedia', 'is'])
PUNCTUATION = re.compile('[%s]' % re.escape(string.punctuation))
STEMMER = Stemmer.Stemmer('english')

def tokenize(text):
  return text.split()

def lowercase_filter(tokens):
  for t in range (len(tokens)):
    tokens[t] = tokens[t].lower()
  return tokens

def punctuation_filter(tokens):

    for t in range(len(tokens)):
      tokens[t] = PUNCTUATION.sub('', tokens[t])

    return tokens

def stopword_filter(tokens):

    stop = []
    for t in tokens:
      if t not in STOPWORDS:
        stop.append(t)
    return stop


def stem_filter(tokens):
    return STEMMER.stemWords(tokens)

def analyze(text):
    tokens = tokenize(text)
    tokens = lowercase_filter(tokens)
    tokens = punctuation_filter(tokens)
    tokens = stopword_filter(tokens)
    tokens = stem_filter(tokens)
    
    results = []

    for token in tokens:
      if token:
        results.append(token)
    return results
