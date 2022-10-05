import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
from joblib import dump, load
from clearml import Dataset
from config.config import AppConfig 
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pathlib import Path


def ab(a,b):
    return a + b


def main_actions(config: AppConfig, logger=None):

    paths = Path(config.dateset_local_path)
    df = pd.DataFrame()
    
    for path in list(paths.glob("*.csv")):
        df_temp = pd.read_csv(path.as_posix())
        df = pd.concat((df, df_temp), axis=0)
    
    df.reset_index(drop=True, inplace=True)
    df.drop(['index'], axis=1, inplace=True)

    X = df.drop(['y'],axis=1)
    y = df.y
    X_train, X_test, y_train, y_test = train_test_split(X, y, 
                                test_size=config.test_size, 
                                random_state=config.random_state)
    model = LogisticRegression(random_state=config.random_state,
                                warm_start=True, 
                                max_iter=config.max_iter)

    acc_train, acc_val = [], []
    for i in range(config.num_iters):
        model.fit(X_train,y_train,)

        acc_epoch_train = accuracy_score(y_train, model.predict(X_train))
        acc_epoch_val = accuracy_score(y_test, model.predict(X_test))

        acc_train.append(acc_epoch_train)
        acc_val.append(acc_epoch_val)

        if logger:
            logger.report_scalar(title="Train", 
                    series="series A", iteration=i, value=acc_epoch_train)
            logger.report_scalar(title="Test", 
                    series="series A", iteration=i, value=acc_epoch_val)

    plt.plot(acc_train, label='Train',color='red')
    plt.plot(acc_val, label='Test', color='blue')
    plt.title('accuracy score')
    plt.xlabel('epoch')
    plt.grid()
    plt.legend()
    plt.show()

    assert acc_val[-1]>0.9, 'Model bad'
    
    dump(model, '/app/models/model.joblib')

    
def main():
    config = AppConfig.parse_raw()
    main_actions(config=config)


if __name__=='__main__':
    main()
