def ab(a,b):
    return a + b

from joblib import dump, load
from clearml import Dataset
from config.config import AppConfig 
import pandas as pd 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from pathlib import Path
import numpy as np


def main_actions(config: AppConfig):

    paths = Path(config.dateset_local_path)
    df = pd.DataFrame()
    
    for path in list(paths.glob("*.csv")):
        df_temp = pd.read_csv(path.as_posix())
        df = pd.concat((df, df_temp), axis=0)
        # df = df.append(pd.read_csv(path.as_posix()))
    df.reset_index(drop=True, inplace=True)
    df.drop(['index'], axis=1, inplace=True)

    X = df.drop(['y'],axis=1)
    y = df.y
    model = LogisticRegression(random_state=config.random_state, max_iter=10**4)
    model.fit(X,y)
    dump(model, '/app/models/model.joblib') 


def main():
    config = AppConfig.parse_raw()
    main_actions(config=config)


if __name__=='__main__':
    main()