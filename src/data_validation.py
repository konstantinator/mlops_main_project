import pandas as pd 
import numpy as np
from clearml import Dataset
from config.config import AppConfig 
from pathlib import Path


def main_actions(config: AppConfig):

    paths = Path(config.dateset_local_path)
    df = pd.DataFrame()
    
    for path in list(paths.glob("*.csv")):
        df_temp = pd.read_csv(path.as_posix())
        df = pd.concat((df, df_temp), axis=0)
    
    df.reset_index(drop=True, inplace=True)
    df.drop(['index'], axis=1, inplace=True)

    assert df.isna().sum().sum()==0, 'Include nan'


def main():
    config = AppConfig.parse_raw()
    main_actions(config=config)


if __name__=='__main__':
    main()
