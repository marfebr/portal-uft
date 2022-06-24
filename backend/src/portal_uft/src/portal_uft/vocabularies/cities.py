from zope.interface import provider
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary

# import requests


CITIES = [
    ("palmas", "Palmas"),
    ("gurupi", "Gurupi"),
    ("miracema", "Miracema"),
    ("portonacional", "Porto Nacional"),
]


# def busca_cidades():# -> List[List[str]]:
#     url = "https://servicodados.ibge.gov.br/api/v1/localidades/estados/TO/municipios"
#     resp =  requests.get(url)
#     data = resp.json()
#     return [(cidade[id], cidade['nome']) for cidade in data ]

# CITIES = busca_cidades()


@provider(IVocabularyFactory)
def cities_vocabulary(context):
    """Vocabulary of cities im TO"""
    terms = []
    for token, title in CITIES:
        terms.append(SimpleTerm(token, token, title))
    return SimpleVocabulary(terms)
