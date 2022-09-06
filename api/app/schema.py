from pydantic import BaseModel,root_validator
from typing import List

class movie(BaseModel):
    
    
    imdbID:str
    Title:str
    Plot:str
    imdbRating:str

    @root_validator(pre=True)
    def get_source(cls,values):
        values=values['_source']
        return values
        


class result(BaseModel):
    total:int
    movies:List[movie]

    @root_validator(pre=True)
    def get_total(cls,values):
        values=values['hits']
        values['total']=values['total']['value']
        values['movies']=values['hits']
        return values