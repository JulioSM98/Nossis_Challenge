
from pandas import read_csv
from elasticsearch import Elasticsearch
import requests
from os import environ


def get_info(id):
    api_url=f"http://www.omdbapi.com/?i={id}&apikey={environ['API_KEY']}"
    response = requests.get(api_url)
    return response.json()

def add_row_es(dict_data):
    es = Elasticsearch(hosts=[{"host":'db',"port":9200,'scheme':'http'}],headers={"accept": "application/vnd.elasticsearch+json; compatible-with=7"}, verify_certs=False)
    es.snapshot.create_repository(name='jsm',settings={
      "location": "jsm",
      "max_restore_bytes_per_sec": "40mb",
      "readonly": "false",
      "compress": "true",
      "max_snapshot_bytes_per_sec": "40mb"
    })
    resp= es.index(index='movies_api',document=dict_data)
    return resp



def add_data():
    if environ['API_KEY'] != 'none':
        data = read_csv('./data_loader/data.tsv',sep='\t', header=0,dtype=str)
        dataframe = data[data['titleType']=='movie']
        for data in dataframe.head(1000).to_dict(orient='records'):
            print(add_row_es(get_info(data['tconst'])))
