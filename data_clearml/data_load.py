from sklearn.datasets import load_iris
import pandas as pd
import numpy as np

def main():
    X,y = load_iris(return_X_y=True)
    X_full = np.concatenate((X, y.reshape(-1, 1)), axis=1)
    df = pd.DataFrame(X_full, 
                        columns=['sl', 'sw', 'pl', 'pw', 'y'],)
    df.loc[:,'y'] = df.loc[:,'y'].astype(int)
    breakpoint()

    df = df.sample(150).reset_index()
    parts = 15
    shape_parts = df.shape[0] // parts
    for i in range(parts):
        df.iloc[i * shape_parts : (i + 1) * shape_parts].to_csv(f'/app/data/{i}.csv', index=False)
    #breakpoint()



if __name__=='__main__':
    main()