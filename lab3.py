import pandas as pd
import numpy as np

def average(list):
    0 if len(list) == 0 else sum(list) / len(list)

def countValues(X_train, X_test, y_train, y_test ):
    print('ilośc wartości x_train: ', X_train.size)
    print('ilośc wartości X_test: ', X_test.size)
    print('ilośc wartości y_train: ', y_train.size)
    print('ilośc wartości y_test: ', y_test.size)

def countUniqueValues(X_train, X_test, y_train, y_test ):
    print('ilośc unikalnych wartości x_train: ', np.unique(X_train).size)
    print('ilośc unikalnych wartości X_test: ', np.unique(X_test).size)
    print('ilośc unikalnych wartości y_train: ', np.unique(y_train).size)
    print('ilośc unikalnych wartości y_test: ', np.unique(y_test).size)

def average(X_train, X_test, y_train, y_test ):
    print('ilośc srednia wartości x_train: ', X_train.mean())
    print('ilośc srednia wartości X_test: ', X_test.mean())
    print('wartości srednia z y_train: ', y_train.mean())
    print('wartości srednia z y_test: ', y_test.mean())

def minMaxValues(X_train, X_test, y_train, y_test):
    print('wartości min z x_train: ', X_train.min())
    print('wartości max z x_train: ', X_train.max())
    print('wartości min z  X_test: ', X_test.min())
    print('wartości max z  X_test: ', X_test.max())
    print('wartości min z  y_train: ', y_train.min())
    print('wartości max z  y_train: ', y_train.max())
    print('wartości min z  y_test: ', y_test.min())
    print('wartości max z  y_test: ', y_test.max())

def sumNotNull(X_train, X_test, y_train, y_test):
    print('ilosc wartosci null z x_train: ', X_train.isnull().sum())
    print('ilosc wartosci null z X_test: ', X_test.isnull().sum())
    print('ilosc wartosci null z y_train: ', y_train.isnull().sum())
    print('ilosc wartosci null z y_test: ', y_test.isnull().sum())

def mostCommon(X_train, X_test, y_train, y_test):
    print('najczęściej występująca w x_train: ')
    mostCommonData(X_train)
    print('najczęściej występująca w X_test: ')
    mostCommonData(X_test)
    print('najczęściej występująca w y_train: ')
    mostCommonData(y_train)
    print('najczęściej występująca w y_test: ')
    mostCommonData(y_test)

def mostCommonData(data):
    for col in data.columns:
        print(col)
        print(data[col].mode().tolist())

if __name__ == '__main__':

    X_train = pd.read_csv('out/X_train.csv')
    X_test = pd.read_csv('out/X_test.csv')
    y_train = pd.read_csv('out/y_train.csv')
    y_test = pd.read_csv('out/y_test.csv')

    countValues(X_train, X_test, y_train, y_test)
    countUniqueValues(X_train, X_test, y_train, y_test)
    minMaxValues(X_train, X_test, y_train, y_test)
    average(X_train, X_test, y_train, y_test)
    sumNotNull(X_train, X_test, y_train, y_test)
    mostCommon(X_train, X_test, y_train, y_test)