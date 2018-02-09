import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

print('numpy')
start_date = '2017-02-01'
end_date = '2018-01-01'
dates = pd.date_range(start_date, end_date)
# create a dataframe with exisitng dates
df1 = pd.DataFrame(index=dates)

# INDEX IS AN INTEGER CONVERT TO DATE
dfSPY = pd.read_csv("data/SPY.csv",
                    index_col="Date",
                    parse_dates=True,
                    usecols=['Date','Adj Close'],
                    na_values=['nan'])
# Use join to combine stocks
dfSPY = dfSPY.rename(columns={'Adj Close': 'SPY'})
df1 = df1.join(dfSPY, how='inner')

symbols = ['NVDA','AAPL','GOOG']

for symbol in symbols:
    df_sym = pd.read_csv(
        'data/{}.csv'.format(symbol),
        index_col='Date',
        parse_dates=True,
        usecols=['Date','Adj Close'],
        na_values=['nan'])
    df_sym = df_sym.rename(columns={"Adj Close": symbol})
    df1 = df1.join(df_sym)

ax = df1.plot(title='Stock Prices')
ax.set_xlabel('Date')
ax.set_ylabel('Price')
plt.show()


