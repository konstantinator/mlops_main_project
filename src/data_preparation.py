from clearml import Dataset
from config.config import AppConfig 
import pandas as pd 
import clearml


def main_actions(config: AppConfig):

    paths = Path(config.dateset_local_path)
    df = pd.DataFrame()
    
    for path in list(paths.glob("*.csv")):
        df_temp = pd.read_csv(path.as_posix())
        df = pd.concat((df, df_temp), axis=0)

    df.reset_index(drop=True, inplace=True)
    df.drop(['index'], axis=1, inplace=True)

    X, y = df.drop(['y'], axis=1).values, df['y'].values
    scaler = StandardScaler()
    X = scaler.fit_transform(X)
    X_full = np.concatenate((X, y.reshape(-1, 1)), axis=1)
    
    df = pd.DataFrame(X_full, 
                        columns=['sl', 'sw', 'pl', 'pw', 'y'],)
    df.loc[:,'y'] = df.loc[:,'y'].astype(int)
   #breakpoint()

    df = df.sample(150).reset_index()
    parts = 3
    shape_parts = df.shape[0] // parts
    for i in range(parts):
        df.iloc[i * shape_parts : (i + 1) * shape_parts].to_csv(f'/app/data_prep/{i}.csv', index=False)


def main():
    config = AppConfig.parse_raw()
    main_actions(config=config)


if __name__ == "__main__":
    main()
