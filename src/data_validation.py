from clearml import Dataset
from config.config import AppConfig 
import pandas as pd 
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

    
    assert df.isna().sum().sum()==0, 'Include nan'

    # for index, row in df.iterrows():
    #     print(type(row['y'].values))
    #     assert type(row['sl'])==np.float, 'not float'
    #     assert type(row['sw'])==np.float, 'not float'
    #     assert type(row['pl'])==np.float, 'not float'
    #     assert type(row['pw'])==np.float, 'not float'
    #     assert type(row['y'])==np.int, 'not int'
        


def main():
    config = AppConfig.parse_raw()
    main_actions(config=config)


if __name__=='__main__':
    main()
