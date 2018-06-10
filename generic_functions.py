import pandas as pd


def percConvert(ser):
  return ser/float(ser[-1])*100

def readLoanHistoryFile() :
  return readFileIntoPandasDataframe("dataset\\train_loanprediction.csv")

def readFileIntoPandasDataframe(fileName , header=0) :
  return pd.read_csv(fileName , header=header)

