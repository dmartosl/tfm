# -*- coding: utf-8 -*-
"""stanza.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rzWyrj1NxMxKqiRdM13XjmXB_-whDYyN
"""

!pip install stanza

import stanza

stanza.download('es', verbose=False)
es_nlp = stanza.Pipeline('es', verbose=False, use_gpu=True)

import requests

file_url = 'https://raw.githubusercontent.com/dmartosl/tfm/master/data/SPACCC/corpus/S0004-06142005000400011-1.txt'
page = requests.get(file_url)
page.text

es_doc = es_nlp(page.text)
print(type(es_doc))

es_doc

for i, sent in enumerate(es_doc.sentences):
    print("[Sentence {}]".format(i+1))
    for word in sent.words:
        print("{:12s}\t{:12s}\t{:6s}\t{:d}\t{:12s}".format(\
              word.text, word.lemma, word.pos, word.head, word.deprel))
    print("")

print("Mention text\tType\tStart-End")
for ent in es_doc.ents:
    print("{}\t{}\t{}-{}".format(ent.text, ent.type, ent.start_char, ent.end_char))

word = es_doc.sentences[0].words[0]
print(word)

stanza.download('en', package='mimic', processors={'ner': 'i2b2'})
nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'})
doc = nlp(page.text)
doc.sentences[0].print_dependencies()

for ent in doc.entities:
    print(f'{ent.text}\t{ent.type}')

stanza.download('en', package='craft', processors={'ner': 'i2b2'})
nlp = stanza.Pipeline('en', package='craft', processors={'ner': 'i2b2'})
doc = nlp(page.text)
for ent in doc.entities:
    print(f'{ent.text}\t{ent.type}')

!pip install googletrans==3.1.0a0

from googletrans import Translator

translator = Translator()
translation = translator.translate(page.text, src='es', dest='en')

page.text

translation.text

stanza.download('en', package='craft', processors={'ner': 'i2b2'})
nlp = stanza.Pipeline('en', package='craft', processors={'ner': 'i2b2'})
doc = nlp(translation.text)
for ent in doc.entities:
    print(f'{ent.text}\t{ent.type}')

stanza.download('en', package='mimic', processors={'ner': 'i2b2'})
nlp = stanza.Pipeline('en', package='mimic', processors={'ner': 'i2b2'})
doc = nlp(translation.text)
for ent in doc.entities:
    print(f'{ent.text}\t{ent.type}')

