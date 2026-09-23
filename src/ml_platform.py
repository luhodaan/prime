# classe model per i modelli che avrà:
# field bool per indicare se in prod o no 
# risultato su metriche di riferimento
# versione e id ovviamente

# funzione di selezione candidato se modello in prod non presente
# riceverà come parametri una lista di modelli in produzione 
# il candidato
# metriche a cui fare riferimento e soglia minima di performance

from dataclasses import dataclass
from typing import List

@dataclass
class Model:
    name:str
    version:int
    metrics:dict
    stage:str

def model_selector(models_list:list[Model],candidate:Model,metric:str,min_improvement:float) -> Model | None:
    prod_models = [model for model in models_list if model.stage == "prod"]
    if not prod_models:
        return candidate
    return None

