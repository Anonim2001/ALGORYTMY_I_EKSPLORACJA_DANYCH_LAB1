from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
import pandas

def getWine():
    return load_wine()

def saveInCSV(data, names, filename):
    df = pandas.DataFrame(data, columns=names)
    df.to_csv('out/'+filename, index=False)

def splitDatasets(wine):
    X_train, X_test, y_train, y_test = train_test_split(
        wine.data,wine.target, test_size = 0.4)
    return X_train, X_test, y_train, y_test

if __name__ == '__main__':
    wine = getWine()
    X_train, X_test, y_train, y_test = splitDatasets(wine)
    saveInCSV(X_train, wine.feature_names, 'X_train.csv')
    saveInCSV(X_test, wine.feature_names, 'X_test.csv')
    target_columns = ['target', ]
    saveInCSV(y_train, target_columns, 'y_train.csv')
    saveInCSV(y_test, target_columns,'y_test.csv')