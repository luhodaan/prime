# primo test più triviale, andremo a verificare che in caso di modello non presente in prod
#restituiamo il candidato come modello disponibile

from src.ml_platform import Model, model_selector


def test_always_candidate_if_no_prod():
    production_models = []
    candidate = Model(name="churn_pred",version=1,metrics= {"auc":0.8},stage="pre-prod")
    result_model = model_selector(production_models,candidate,metric="auc",min_improvement=0.05)
    assert candidate == result_model