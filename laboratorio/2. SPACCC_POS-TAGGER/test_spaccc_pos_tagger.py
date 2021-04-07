from Med_Tagger import Med_Tagger
import requests
import json


if __name__ == "__main__":
    tag = Med_Tagger()
    file_url = 'https://raw.githubusercontent.com/dmartosl/tfm/master/data/SPACCC/corpus/S0004-06142005000400011-1.txt'
    page = requests.get(file_url)
    file_text = page.text
    #print(file_text)
    print(tag.parse(file_text))
    #print(json.dumps(tag.parse(file_text), sort_keys=True, indent=4))
    del(tag)
