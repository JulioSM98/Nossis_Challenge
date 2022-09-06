from typing import Union
from depends import ES
from fastapi import FastAPI
from schema import movie, result
from data_loader.data_loader import add_data

app = FastAPI(
  title="Nosis Challenge",
  docs_url="/"
)


@app.get("/all_movies",response_model=result)
def Get_all_movies(q:Union[int,None]=10):
    db=ES.search(index='movies_api',body={
      "query": {
        "query_string": {
          "query": "*"
        }
      },
      "size": q,
      "from": 0,
      
    })
    return db


@app.get("/movie",response_model=result)
def get_movie_title(title_movie: str, q: Union[int, None] = 5):
    db=ES.search(index='movies_api',body={
  "query": {
    "query_string": {
      "query": f"Title:{title_movie}"
    }
  },
  "size": q,
  "from": 0,
  
})
  
    return db

@app.on_event("startup")
async def _startup_event():
  add_data()