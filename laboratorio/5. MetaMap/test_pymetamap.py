from pymetamap import MetaMapLite
import os
import requests
from googletrans import Translator

file_url = 'https://raw.githubusercontent.com/dmartosl/tfm/master/data/SPACCC/corpus/S0004-06142005000400011-1.txt'
page = requests.get(file_url)

text = page.text
print(text)

translator = Translator()
translation = translator.translate(text, src='es', dest='en')
print(translation.text)

print(os.getcwd())
os.chdir('/home/uned/public_mm_lite/')
print(os.getcwd())

mm = MetaMapLite.get_instance('/home/uned/public_mm_lite/')
sents = [translation.text]
concepts,error = mm.extract_concepts(sents, [1,2])
for concept in concepts:
    print(concept)
