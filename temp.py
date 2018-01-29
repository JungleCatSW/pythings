# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt


def get_close_max(symbol):
    df = pd.read_csv("GOOG.csv")
    return df['Close'].max()

def test_run():
    df = pd.read_csv("GOOG.csv")
    print(df.head()) #print 
    df[['Close','Adj Close']].plot()
    plt.show()
    
#test_run()
print(get_close_max("GOOG"))
test_run()
