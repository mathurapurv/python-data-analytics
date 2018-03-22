import pandas as pd


def percConvert(ser):
  return ser/float(ser[-1])*100

def readLoanHistoryFile() :
  return pd.read_csv("dataset\\train_loanprediction.csv")