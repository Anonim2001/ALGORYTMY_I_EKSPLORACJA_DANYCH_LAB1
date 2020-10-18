from sklearn.datasets import load_wine
import pandas as pd

def getWine():
    return load_wine()

if __name__ == '__main__':
    data = getWine()
    print(data)
    print(data.target)
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['target'] = data.target
    df.head()
    df.info()