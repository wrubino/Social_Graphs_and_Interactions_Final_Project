import json

from config import Config
from wojciech.lowercase import lowercase


def load_data_wiki():
    with open(Config.Path.full_wiki_data) as file:
        drug_database = json.load(file)

    wiki_properties = [
        'name',
        'categories',
        'content',
        'links',
        'synonyms',
        'url',
    ]

    wiki_data = {prop: list() for prop in wiki_properties}

    for drug, drug_data in drug_database.items():
        data = drug_data['data']
        wiki_data['name'].append(drug.lower())
        wiki_data['categories'].append(lowercase(data['categories']))
        wiki_data['content'].append(data['content'].lower())
        wiki_data['links'].append({key.lower(): value
                                   for key, value in data['links'].items()})
        wiki_data['synonyms'].append(lowercase(data['redirects']))

        wiki_data['url'].append(data['url'])

    return wiki_data
